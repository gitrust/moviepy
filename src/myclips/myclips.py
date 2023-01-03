#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

def create_clip(filename):
    clip = VideoFileClip(filename)
    duration = round(clip.duration)
    w,h = clip.size

    # length of subclip in seconds
    cliplen = 3
    if duration < 3:
        cliplen = duration

    start_clip = 0

    # create new clip starting in the middle of original
    mid = round(duration/2)
    if mid > (cliplen*2):
        start_clip = mid

    end_clip = start_clip + cliplen
    clip = clip.without_audio().subclip(start_clip,end_clip)


    if w > 600:
        clip = clip.fx( vfx.resize, width = 600)
    if h > 600:
        clip = clip.fx( vfx.resize, height = 500)

    time_str = str(datetime.timedelta(seconds=duration, microseconds=0, milliseconds=0))
    return with_text(clip, time_str)

def compose_clips(clips):
    fade_duration = 1 # 1-second fade-in for each clip
    #clips = [clip.crossfadein(fade_duration) for clip in clips]
    #clip = concatenate_videoclips(clips) did not work
    clip = concatenate(clips, padding = -fade_duration,method="compose")
    return clip

def find_clips(dir):
    clips = []
    for root, dirnames, filenames in os.walk(dir):
        for filename in fnmatch.filter(filenames, '*.avi'):
            f = os.path.join(root, filename)
            print("Found " + f)
            try:
                clips.append(create_clip(f))
            except:
                print("Error")
                continue
            if len(clips) > 10:
                break
    return clips

def main(argv):
    clips = find_clips(argv[0])
    if len(clips) > 0:
        clip = compose_clips(clips)
        # , bitrate="500k",codec="mpeg4"
        clip.write_videofile("final.mp4", fps=24, bitrate="500k",codec="mpeg4")

if __name__=='__main__':
    main(sys.argv[1:])
