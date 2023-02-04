#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  Zoom into clip
"""

import sys
from moviepy.editor import *


# zoom fx
# clip.fx(zoom,factor=1)
def zoom(clip, factor=1):
    c = (1-1.0/factor) / 2
    x_crop = int(c * clip.w)
    y_crop = int(c * clip.h)
    return clip.crop(x_crop, y_crop, -x_crop, -y_crop).resize(clip.size)


def main(argv):
    clip = zoom(VideoFileClip(argv[0]))
    clip.write_gif(argv[1], fps=5)


if __name__=='__main__':
    main(sys.argv[1:])
