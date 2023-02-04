#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  Convert video to black&white
"""

import sys
from moviepy.editor import *
import moviepy.video.fx.all as vfx

# black and white video
def blacknwhite(clip):
	return clip.fx(vfx.blackwhite)


def main(argv):
    clip = blacknwhite(VideoFileClip(argv[0]))
    clip.write_gif(argv[1], fps=5)


if __name__=='__main__':
    main(sys.argv[1:])
