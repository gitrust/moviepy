#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  Blur video
"""

import sys
from moviepy.editor import *
import moviepy.video.fx.all as vfx
import scipy.ndimage as ndimage

# blur image
# sigma=5 - very blurred
def blur_img(img, sigma=3):
	return ndimage.gaussian_filter(img, sigma)

def blur(clip):
	return clip.fl_image(blur_img)

def main(argv):
    clip = blur(VideoFileClip(argv[0]))
    clip.write_gif(argv[1], fps=5)


if __name__=='__main__':
    main(sys.argv[1:])
