from moviepy.editor import *
import sys


# settings
mytext =   "My Text"
vcodec =   "libx264"
input = "mrbean.mp4"
output = "final.mp4"
# max characters: 18 
txtfontsize = 60

clips = [VideoFileClip(input,audio_buffersize=15000).subclip("00:10:00","00:10:03.6")]

# append textclip to all clips at first position
# Generate a text clip. You can customize the font, color, etc.
# set textclip size from the first video clip
txt_clip = TextClip(mytext,fontsize=txtfontsize,font="Arial",color='white',size=clips[0].size)

# Say that you want it to appear 10s at the center of the screen
txt_clip = txt_clip.set_pos('center').set_duration(4)

fade_duration = 1 # 1-second fade-in for each clip
clips = [clip.crossfadein(fade_duration) for clip in clips]

# The "padding" ensures that the clips will overlap for 1 second
final_clip = concatenate(clips, padding = -fade_duration,method="compose").fadeout(3)

# Write the result to a file
print("Final clip length is " + str(datetime.timedelta(seconds=final_clip.end)))
final_clip.write_videofile(output,fps=24, codec=vcodec,preset="slow",ffmpeg_params=["-crf","26"])
