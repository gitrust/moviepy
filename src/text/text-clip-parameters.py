#!/usr/bin/env python
# -*- coding: utf-8 -*-

import moviepy.editor as mpy

# list all available fonts
print("Available fonts:")
print(mpy.TextClip.list('font'))

# list background colors
print("bg_color:")
print(mpy.TextClip.list('color'))
