from moviepy.editor import *
import sys
import datetime
import subprocess
import os
import moviepy.video.fx.all as vfx
import scipy.ndimage as ndimage

# Combines video files in a given directory to one file with an additional title
#

# settings
vcodec =   "libx264"

# The range of the CRF scale is 0–51, where 0 is lossless, 23 is the default, and 51 is worst quality possible.
# A lower value generally leads to higher quality, and a subjectively sane range is 17–28. 
# Consider 17 or 18 to be visually lossless or nearly so
videoquality = "24"
# slow, ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow
compression = "slow"
# included extensions of files which will be processed
extensions = ["mp4","avi","mov"]


def write(clip,tofile):
        # Write the result to a file
    print("Final clip length is " + str(datetime.timedelta(seconds=clip.end)))
    clip.write_videofile(tofile,threads=4,fps=24, codec=vcodec,preset=compression,ffmpeg_params=["-crf",videoquality])

# blur image
# sigma=5 - very blurred
def blur(img,sigma=3):
	
	return ndimage.gaussian_filter(img, sigma)

# zoom fx
# clip.fx(zoom,factor=1)
def zoom(clip, factor):
    c = (1-1.0/factor) / 2
    x_crop = int(c * clip.w)
    y_crop = int(c * clip.h)
    return clip.crop(x_crop, y_crop, -x_crop, -y_crop).resize(clip.size)

def get_rotation(file_path_with_file_name):
    """
    Function to get the rotation of the input video file.
    Adapted from gist.github.com/oldo/dc7ee7f28851922cca09/revisions using the ffprobe comamand by Lord Neckbeard from
    stackoverflow.com/questions/5287603/how-to-extract-orientation-information-from-videos?noredirect=1&lq=1

    Returns a rotation None, 90, 180 or 270
    """
    cmd = "ffprobe -loglevel error -select_streams v:0 -show_entries stream_tags=rotate -of default=nw=1:nk=1"
    args = cmd.split(" ")
    args.append(file_path_with_file_name)
    # run the ffprobe process, decode stdout into utf-8 & convert to JSON
    ffprobe_output = subprocess.check_output(args).decode('utf-8')
    if len(ffprobe_output) > 0:  # Output of cmdis None if it should be 0
        ffprobe_output = json.loads(ffprobe_output)
        rotation = ffprobe_output

    else:
        rotation = 0

    return rotation
    
def cellphone2wide(clip,newsize):
    w,h = moviesize = clip.size
    movie = vfx.rotate(clip, -90).resize(height=720)

    # background clip, rotated and stretched, blurred, zoom in
    bg = movie.resize(newsize).without_audio().fl_image(blur).fx(zoom,2)
    print(str(bg.size))
    # a compose of both clips
    # position original movie at center
    return CompositeVideoClip([bg,movie.set_pos("center")]).set_duration(movie.duration)
    #return bg

    
def main(argv):
    if len(argv) < 1:
        print("Usage: video.py videofile")
        sys.exit(0)
        
    videofile = argv[0]
    clip = VideoFileClip(videofile,audio_buffersize=15000)
    clip = cellphone2wide(clip,clip.size)
    write(clip,"final.mp4")
    
    
if __name__=='__main__':
    main(sys.argv[1:])