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

    #Eroding and Dilating
    kernel=np.ones((1,1),np.uint8)
    img1e=cv2.erode(img1bb,kernel,iterations=3)
    img1d=cv2.dilate(img1e,kernel,iterations=3)

    imgf=np.float32(img1).reshape(-1,3)
    criteria=(cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,20,1.0)
    compactness,label,center=cv2.kmeans(imgf,5,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
    center=np.uint8(center)
    final_img=center[label.flatten()]
    final_img=final_img.reshape(img1.shape)
    
    # mask edged image with our "BEAUTIFY" image
    return cv2.bitwise_and(img_noise, img_noise, mask=img_edges)
    

def cartoonify(clip):
    return clip.fl_image(cartoonify_img)


def main(argv):
    clip = cartoonify(VideoFileClip(argv[0]))
    clip.write_gif(argv[1], fps=5)


if __name__=='__main__':
    main(sys.argv[1:])
