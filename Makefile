WORKDIR=$(CURDIR)

PYTHON:=docker run -it --rm -v $(WORKDIR)/samples:/opt/app/samples -v $(WORKDIR):/opt/app gitrust/moviepy python

# build docker image
build:
	docker build -t gitrust/moviepy .

# Run docker image
run:
	$(PYTHON) /bin/bash

render-examples: render/sketchy.gif render/sketchy.gif

render/pixelate.gif:
	$(PYTHON) src/pixelate.py samples/bee1.mp4 render/pixelate.gif
	
render/crossfade.gif:
	$(PYTHON) src/crossfade.py samples/bee1.mp4 samples/bee2.mp4 render/crossfade.gif

render/sketchy.gif:
	$(PYTHON) src/sketchy.py samples/bee1.mp4 render/sketchy.gif

render/cartoonify.gif:
	$(PYTHON) src/cartoonify.py samples/bee1.mp4 render/cartoonify.gif

render/zoom.gif:
	$(PYTHON) src/zoom.py samples/bee1.mp4 render/zoom.gif

extract_images:
	$(PYTHON) src/extract_img.py samples/bee1.mp4
	$(PYTHON) src/extract_img.py render/cartoonify.gif
	$(PYTHON) src/extract_img.py render/crossfade.gif
	$(PYTHON) src/extract_img.py render/pixelate.gif
	$(PYTHON) src/extract_img.py render/sketchy.gif
	$(PYTHON) src/extract_img.py render/zoom.gif
