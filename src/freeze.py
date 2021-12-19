#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# freeze a region of video
#
# video taken from:
# * https://youtu.be/HKUY_gOxLas
#
# documentation of the function:
# * https://zulko.github.io/moviepy/_modules/moviepy/video/fx/freeze_region.html

from moviepy.editor import *

clip = (VideoFileClip("mrbean.mp4")
        .subclip("00:23:39.4","00:23:40.6")
        .resize(width=600)
        .fx(vfx.freeze_region, outside_region=(0, 0, 290, 322)))
clip.write_gif("mrbean.gif", fps=15)
