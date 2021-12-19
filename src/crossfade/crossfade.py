from moviepy.editor import *

clips=[]
# Append clips using some video from current directory
# Use only a part of the clip for test purposes
clips.append(VideoFileClip('video1.mp4').subclip(10,15))
clips.append(VideoFileClip('video2.mp4').subclip(30,35))

# 1-second lsfade-in for each clip
fade_duration = 1
clips = [clip.crossfadein(fade_duration) for clip in clips]

# concatenate using compose method, fade out = 3 seconds
myclip =  concatenate(clips, padding = -fade_duration,method="compose").fadeout(3)
myclip.write_videofile("crossfade.mp4", fps=24, bitrate="500k",codec="mpeg4")
