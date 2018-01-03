from moviepy.editor import *
import sys
import datetime
import os

# Combines video files in a given directory to one file with an additional title
#

# settings
vcodec =   "libx264"
filename = "final.mp4"
vlist   = "video.list"

# The range of the CRF scale is 0–51, where 0 is lossless, 23 is the default, and 51 is worst quality possible.
# A lower value generally leads to higher quality, and a subjectively sane range is 17–28. 
# Consider 17 or 18 to be visually lossless or nearly so
videoquality = "23"
# slow, ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow
compression = "slow"
# included extensions of files which will be processed
extensions = ["mp4","avi"]
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

def addtext(clips,text):
	# append textclip to all clips at first position
	# Generate a text clip. You can customize the font, color, etc.
	# set textclip size from the first video clip
	txt_clip = TextClip(text,
			fontsize=txtfontsize,
			font="Arial",
			color='white',
			size=clips[0].size,
			transparent=True).set_pos('center').set_duration(4)
	clips[0] = CompositeVideoClip([clips[0], txt_clip])
	
def files2clips(files):
	clips=[]
	for fname in files:
		# skip comments
		if fname.startswith("#"):
			continue
		print("Add file to clips " + fname)
		clips.append(VideoFileClip(fname,audio_buffersize=15000))
	return clips
	
def convert(clips,tofile):

	# cross fade each clip
	fade_duration = 1 # 1-second 
	clips = [clip.crossfadein(fade_duration) for clip in clips]


	# concat clips
	# The "padding" ensures that the clips will overlap for 1 second
	final_clip = concatenate(clips, padding = -fade_duration,method="compose").fadeout(3)


	# Write the result to a file
	print("Final clip length is " + str(datetime.timedelta(seconds=final_clip.end)))
	final_clip.write_videofile(tofile,fps=24, codec=vcodec,preset=compression,ffmpeg_params=["-crf",videoquality])

def main(argv):
	if len(argv) < 2:
		print("Usage: video.py path text")
		sys.exit(0)
		
	path = argv[0]
	text = argv[1]
	files = listfiles(path)
	
	clips = files2clips(files)
	addtext(clips,text)
	convert(clips,"final.mp4")
	
if __name__=='__main__':
    main(sys.argv[1:])