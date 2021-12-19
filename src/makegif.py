#!/usr/bin/env python
# -*- coding: utf-8 -*-

from moviepy.editor import *


clip = (VideoFileClip("myvideo.mp4")
        .subclip("00:00:10","00:00:15")
        .resize(width=300))
clip.write_gif("my.gif", fps=5)
