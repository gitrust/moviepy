#!/usr/bin/env python
# -*- coding: utf-8 -*-

from moviepy.editor import *


clip = (VideoFileClip("myvideo.mp4").subclip(10,15).resize(width=300))
clip.write_gif("my.gif", fps=5)
