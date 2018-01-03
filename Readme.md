# Collection of movie.py scripts


## Videoeditor moviepy (python basiert)

http://zulko.github.io/moviepy


## Installation of movie.py for ubuntu

	sudo apt-get install ez_setup
	sudo apt-get install python-pip
	sudo apt-get install python-numpy
	sudo pip install moviepy

## Installation of gizeh

	sudo apt-get install python-dev python-pip ffmpeg libffi-dev
	sudo pip install gizeh


## Video Codec

https://zulko.github.io/moviepy/ref/VideoClip/VideoClip.html

Codec to use for image encoding. Can be any codec supported by ffmpeg. 
If the filename is has extension ‘.mp4’, ‘.ogv’, ‘.webm’, the codec will be set 
accordingly, but you can still set it if you don’t like the default. 
For other extensions, the output filename must be set accordingly.

Some examples of codecs are:

* 'libx264' (default codec for file extension .mp4) makes well-compressed videos (quality tunable using ‘bitrate’).

* 'mpeg4' (other codec for extension .mp4) can be an alternative to 'libx264', and produces higher quality videos by default.

* 'rawvideo' (use file extension .avi) will produce a video of perfect quality, of possibly very huge size.

* png (use file extension .avi) will produce a video of perfect quality, of smaller size than with rawvideo

* 'libvorbis' (use file extension .ogv) is a nice video format, which is completely free/ open source. However not everyone has the codecs installed by default on their machine.

* 'libvpx' (use file extension .webm) is tiny a video format well indicated for web videos (with HTML5). Open source.

## rule of thumb for video size

	filesize (in MB) = (bitrate in Mbit/s / 8) * (video length in seconds)



## Installation on Windows

* Install python 3.x
* Install pip for python 3.x
* Install moviepy with pip "pip install moviepy"
* Adapt moviepy configuration for IMAGEMAGICK
** in "PYTHONPATH/lib/site-packages/moviepy/config_defaults.py" or
** or set sys environment variable bevore execution of python script 

    IMAGEMAGICK_BINARY = "C:\\Program Files\\ImageMagick_VERSION\\magick.exe"

## ffmpeg options for hiqh quality encoding

* https://trac.ffmpeg.org/wiki/Encode/H.264