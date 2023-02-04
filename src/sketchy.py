#!/usr/bin/env python
# -*- coding: utf-8 -*-

from moviepy.editor import *
import numpy as np
import cv2

# https://towardsdatascience.com/generate-pencil-sketch-from-photo-in-python-7c56802d8acb


def sketch_img(img):
    k_size = 7
    
    # Convert to Grey Image
    grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Invert Image
    invert_img = cv2.bitwise_not(grey_img)

    # Blur image
    blur_img = cv2.GaussianBlur(invert_img, (k_size,k_size),0)

    # Invert Blurred Image
    invblur_img = cv2.bitwise_not(blur_img)

    # Sketch Image
    return cv2.divide(grey_img, invblur_img, scale=256.0)


def sketchy(clip):
    return clip.fl_image(sketch_img)


def main(argv):
    clip = sketchy(VideoFileClip(argv[0]))
    clip.write_gif(argv[1], fps=5)


if __name__=='__main__':
    main(sys.argv[1:])
