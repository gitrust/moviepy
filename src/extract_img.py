#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from moviepy.editor import *

def extract_frame(video, time, img_path):
    clip = VideoFileClip(video)
    clip.save_frame(img_path, time)


def main(argv):
    extract_frame(argv[0], 0.7, argv[0] + ".jpg")


if __name__=='__main__':
    main(sys.argv[1:])