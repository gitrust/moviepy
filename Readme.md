# Collection of movie.py experiments


## Videoeditor moviepy (based on python)

http://zulko.github.io/moviepy


## Run examples

To run examples using Docker

1. install docker
2. build docker image by `make build`
3. run docker image by `make run`
4. now run examples, e.g. `python src/text/concat-text.py`


## Video Codec

https://zulko.github.io/moviepy/ref/VideoClip/VideoClip.html

Codec to use for image encoding. Can be any codec supported by ffmpeg. 
If the filename is has extension ‘.mp4’, ‘.ogv’, ‘.webm’, the codec will be set 
accordingly, but you can still set it if you don’t like the default. 
For other extensions, the output filename must be set accordingly.

Some examples of codecs are:

* 'libx264' (default codec for file extension .mp4) makes well-compressed videos (quality tunable using ‘bitrate’)
* 'mpeg4' (other codec for extension .mp4) can be an alternative to 'libx264', and produces higher quality videos by default
* 'rawvideo' (use file extension .avi) will produce a video of perfect quality, of possibly very huge size
* png (use file extension .avi) will produce a video of perfect quality, of smaller size than with rawvideo
* 'libvorbis' (use file extension .ogv) is a nice video format, which is completely free/ open source. However not everyone has the codecs installed by default on their machine
* 'libvpx' (use file extension .webm) is tiny a video format well indicated for web videos (with HTML5). Open source

## rule of thumb for video size

	filesize (in MB) = (bitrate in Mbit/s / 8) * (video length in seconds)

## ffmpeg options for hiqh quality encoding

* https://trac.ffmpeg.org/wiki/Encode/H.264


# References

- Some sample videos are taken from https://www.pexels.com
- https://www.pexels.com/video/close-up-view-of-a-lava-lamp-2000817/
- https://www.pexels.com/video/water-abstract-art-oil-drops-4156092/
