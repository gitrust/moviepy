#!/usr/bin/env python
# -*- coding: utf-8 -*-

from moviepy.editor import *
import numpy as np
import cv2


# https://towardsdatascience.com/generate-pencil-sketch-from-photo-in-python-7c56802d8acb



def sketch_img(img):
    k_size = 7
    #Read Image
    #img=cv2.imread(img)
    
    # Convert to Grey Image
    grey_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Invert Image
    invert_img=cv2.bitwise_not(grey_img)


    # Blur image
    blur_img=cv2.GaussianBlur(invert_img, (k_size,k_size),0)

    # Invert Blurred Image
    invblur_img=cv2.bitwise_not(blur_img)


    # Sketch Image
    sketch_img=cv2.divide(grey_img, invblur_img, scale=256.0)

    return sketch_img

    # convert from numpy rgb array to Pillow Image
    #image = Image.fromarray(img.astype('uint8'), 'RGB')
    
    # resize it to a relatively tiny size
    #image_tiny = image.resize((50,50))
    
    # pixeliztion is resizing a smaller image into a larger one with some resampling
    # convert back from Pillow Image to numpy array
    #return np.asarray(image_tiny.resize(image.size,Image.NEAREST))
    
def sketchy(clip):
    return clip.fl_image(sketch_img)

def main(argv):
    clip = sketchy(VideoFileClip(argv[0]))
    clip.write_gif(argv[1], fps=5)


if __name__=='__main__':
    main(sys.argv[1:])
