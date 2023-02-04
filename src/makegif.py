#!/usr/bin/env python
# -*- coding: utf-8 -*-

from moviepy.editor import *


clip = (VideoFileClip("input.mp4")
# shorten final clip and resize
clipend = min(5, clip.end)
clip = clip.subclip(0,clipend).resize(width=300))

clip.write_gif("final.gif", fps=5)
