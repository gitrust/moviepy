#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Cartoonify effect

    Greyscale -> Blur -> Detect Edges -> Mask -> Cartoon
"""

from moviepy.editor import *
import numpy as np
import cv2

def cartoonify_img(img):
    # convert to rgb format
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # convert to grayscale
    img_grayscale = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    # smooth image
    img_blur = cv2.medianBlur(img_grayscale, 5)

    # detect edges
    img_edges = cv2.adaptiveThreshold(img_blur, 255, 
      cv2.ADAPTIVE_THRESH_MEAN_C, 
      cv2.THRESH_BINARY, 9, 9)

    # remove noise 
    # keep edges sharp
    img_noise = cv2.bilateralFilter(img_rgb, 9, 300, 300)
    
    # mask edged image with our "BEAUTIFY" image
    return cv2.bitwise_and(img_noise, img_noise, mask=img_edges)
    
def cartoonify_v2_img(img):
    # convert to rgb format
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # convert to grayscale
    img_grayscale = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    # smooth image
    img_blur = cv2.medianBlur(img_grayscale, 5)

    # detect edges
    img_edges = cv2.adaptiveThreshold(img_blur, 255, 
      cv2.ADAPTIVE_THRESH_MEAN_C, 
      cv2.THRESH_BINARY, 9, 9)

    # remove noise 
    # keep edges sharp
    img_noise = cv2.bilateralFilter(img_rgb, 9, 300, 300)

    # Eroding
    kernel = np.ones((1,1), np.uint8)
    # diminish features of an image
    img_erode = cv2.erode(img_noise, kernel, iterations=3)
    # increases object area to accentuate features
    img_dilate = cv2.dilate(img_erode, kernel, iterations=3)

    # Color quantization
    img_f = np.float32(img_dilate).reshape(-1,3)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
    compactness,label,center=cv2.kmeans(img_f, 5, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    final_img = center[label.flatten()]
    final_img = final_img.reshape(img_dilate.shape)

    # style img
    final_img = cv2.stylization(final_img, sigma_s=150, sigma_r=0.25)
    
    # mask edged image with beauty image
    return cv2.bitwise_and(final_img, final_img, mask=img_edges)

def cartoonify(clip):
    return clip.fl_image(cartoonify_v2_img)


def main(argv):
    clip = cartoonify(VideoFileClip(argv[0]))
    clip.write_gif(argv[1], fps=5)


if __name__=='__main__':
    main(sys.argv[1:])
