#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   Compose a new video of a collection of video subclips found in specified directory.
"""

import fnmatch
import os
import sys
import datetime

from moviepy.editor import *
import moviepy.video.fx.all as vfx


def with_text(video_clip, text):
    # Generate a text clip
    txt_clip = TextClip(text, fontsize = 30, font = 'DejaVu-Serif', color = 'white')

    # setting position of text in the center and duration will be 1 seconds
    txt_clip = txt_clip.set_pos('center').set_duration(1)

    # Overlay the text clip on the first video clip
    return CompositeVideoClip([video_clip, txt_clip])

def create_clip(filename, cliplen=3):
    clip = VideoFileClip(filename)
    duration = round(clip.duration)
    w,h = clip.size

    # length of subclip in seconds
    if duration < 3:
        cliplen = duration

    start_clip = 0

    # create new clip starting in the middle of original
    mid = round(duration/2)
    if mid > (cliplen*2):
        start_clip = mid

    end_clip = start_clip + cliplen
    clip = clip.without_audio().subclip(start_clip,end_clip)

    # make clips fit into a given size
    if w > 600:
        clip = clip.fx( vfx.resize, width = 600)
    if h > 600:
        clip = clip.fx( vfx.resize, height = 500)

    # render clip duration in seconds
    time_str = str(datetime.timedelta(seconds=duration, microseconds=0, milliseconds=0))
    return with_text(clip, time_str)

def compose_clips(clips):
    fade_duration = 1 # 1-second fade-in for each clip
    return concatenate(clips, padding = -fade_duration,method="compose")

def find_clips(dir, ext):
    """
        Find video files in specified directory, filter by extension
    """
    clips = []
    for root, dirnames, filenames in os.walk(dir):
        for filename in fnmatch.filter(filenames, ext):
            f = os.path.join(root, filename)
            print("Found " + f)
            try:
                clips.append(create_clip(f))
            except:
                print("Error")
                continue
    return clips

def main(argv):
    clips = find_clips(argv[0], '*.avi')
    if len(clips) > 0:
        clip = compose_clips(clips)
        clip.write_videofile("final.mp4", fps=24, bitrate="500k",codec="mpeg4")

if __name__=='__main__':
    main(sys.argv[1:])
