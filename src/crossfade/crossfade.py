#!/usr/bin/env python
# -*- coding: utf-8 -*-

from moviepy.editor import *


def crossfade(clips):
    # 1-second lsfade-in for each clip
    fade_duration = 1
    clips = [clip.crossfadein(fade_duration) for clip in clips]

    # concatenate using compose method, fade out = 2 seconds
    return concatenate(clips, padding = -fade_duration,method="compose").fadeout(2)

def video_clip(file):
    return VideoFileClip(file).without_audio().subclip(t_end=5)

def main(argv):
    clips=[]
    clips.append(video_clip(argv[0]))
    clips.append(video_clip(argv[1]))
    
    finalclip = crossfade(clips)
    finalclip.write_gif(argv[2], fps=5)


if __name__=='__main__':
    main(sys.argv[1:])
