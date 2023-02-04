#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Compose a new clip of multiple clips, fading them and using fadeout effect
"""

from moviepy.editor import *
import sys


def concat(clips):
    clips = [clip.crossfadein(fade_duration) for clip in clips]

    # The "padding" ensures that the clips will overlap for 1 second
    return concatenate(clips, padding = -fade_duration, method="compose").fadeout(3)

def main(argv):
    clips=[]
    clips.append(video_clip(argv[0]))
    clips.append(video_clip(argv[1]))
    
    finalclip = concat(clips)
    finalclip.write_gif(argv[2], fps=5)


if __name__=='__main__':
    main(sys.argv[1:])