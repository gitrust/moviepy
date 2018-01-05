from moviepy.editor import *
import sys
import datetime
import os
import moviepy.video.fx.all as vfx
import scipy.ndimage as ndimage

# Combines video files in a given directory to one file with an additional title
#

# settings
vcodec =   "libx264"
filename = "final.mp4"
vlist   = "video.list"

# The range of the CRF scale is 0–51, where 0 is lossless, 23 is the default, and 51 is worst quality possible.
# A lower value generally leads to higher quality, and a subjectively sane range is 17–28. 
# Consider 17 or 18 to be visually lossless or nearly so
videoquality = "24"
# slow, ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow
compression = "slow"
# included extensions of files which will be processed
extensions = ["mp4","avi","mov"]
# max characters: 18 
txtfontsize = 60


def listfiles(path):
	f=[]
	for root, dirs, files in os.walk(path):  
		for filename in sorted(files):
			# filter only movie files
			if any(filename.lower().endswith(x) for x in extensions):
				f.append(filename)				
	return f

# add centered title at the beginning of the clip
def addtext(clip,text):
	# Generate a text clip. You can customize the font, color, etc.
	# set textclip size from the first video clip
	txt_clip = TextClip(text,
			fontsize=txtfontsize,
			font="Arial",
			color='white',
			transparent=True).set_pos('center').set_duration(4)
	return CompositeVideoClip([clip, txt_clip])
	
def files2clips(files):
	clips=[]
	for fname in files:
		# skip comments
		if fname.startswith("#"):
			continue
		print("Add file to clips " + fname)
		clips.append(VideoFileClip(fname,audio_buffersize=15000))
	return clips

# blur image
# sigma=5 - very blurred
def blur(img,sigma=3):
	
	return ndimage.gaussian_filter(img, sigma)

	
def crossfade(clips):
	
	# cross fade each clip
	fade_duration = 1 # 1-second 
	clips = [clip.crossfadein(fade_duration) for clip in clips]

	# concat clips
	# The "padding" ensures that the clips will overlap for 1 second
	return  concatenate(clips, padding = -fade_duration,method="compose")

# black and white video
def blacknwhite(clip):
	return clip.fx(vfx.blackwhite)

def write(clip,tofile):
		# Write the result to a file
	print("Final clip length is " + str(datetime.timedelta(seconds=clip.end)))
	clip.write_videofile(tofile,threads=4,fps=24, codec=vcodec,preset=compression,ffmpeg_params=["-crf",videoquality])

# zoom fx
# clip.fx(zoom,factor=1)
def zoom(clip, factor):
    c = (1-1.0/factor) / 2
    x_crop = int(c * clip.w)
    y_crop = int(c * clip.h)
    return clip.crop(x_crop, y_crop, -x_crop, -y_crop).resize(clip.size)
	
def withaudio(clip,audiofile):
	audio = AudioFileClip(audiofile)
	clip.set_audio(audio)
	
def blurclip(clip):
	return clip.fl_image(blur)

# rotate a cellphone video
#
# add blurred background video
# Info: using angle of 90 causes an error
# Consider aspect ratio of original videos
def cellphone_rotate(clip,newsize,angle):
	# original clip, rotated
	w,h = moviesize = clip.size
	movie = clip.fx(vfx.rotate,angle,expand=True).resize(height=newsize[1])

	# background clip, rotated and stretched, blurred, zoom in
	bg = movie.resize(newsize).without_audio().fl_image(blur).fx(zoom,2)

	# a compose of both clips
	# position original movie at center
	return CompositeVideoClip([bg,movie.set_pos("center")]).set_duration(movie.duration)

	
def main(argv):
	if len(argv) < 2:
		print("Usage: video.py path-to-videos text")
		sys.exit(0)
		
	path = argv[0]
	text = argv[1]
	
	files = listfiles(path)
	clips = files2clips(files)
	clip = crossfade(clips)
	#clip = blacknwhite(clip)
	#clip = blurclip(clip)
	
	clip = cellphone_rotate(clip,(1024,768),-89.99999999)
	clip = addtext(clip,text)
	clip = clip.fadeout(3)
	write(clip,"final.mp4")
	
	
if __name__=='__main__':
    main(sys.argv[1:])