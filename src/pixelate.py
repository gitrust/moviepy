#!/usr/bin/env python
# -*- coding: utf-8 -*-

from moviepy.editor import *
import numpy as np
from PIL import Image

def pixelate_img(img):

    # convert from numpy rgb array to Pillow Image
    image = Image.fromarray(img.astype('uint8'), 'RGB')
    
    # resize it to a relatively tiny size
    image_tiny = image.resize((50,50))
    
    # pixeliztion is resizing a smaller image into a larger one with some resampling
    # convert back from Pillow Image to numpy array
    return np.asarray(image_tiny.resize(image.size, Image.NEAREST))
    
def pixelate(clip):
    return clip.fl_image(pixelate_img)

def main(argv):
    clip = pixelate(VideoFileClip(argv[0]))
    clip.write_gif(argv[1], fps=5)


if __name__=='__main__':
    main(sys.argv[1:])
