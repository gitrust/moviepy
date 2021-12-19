WORKDIR=$(shell pwd)

# build docker image
build:
	docker build -t moviepy:latest .

# Run docker image
run:
	docker run -it --rm -v $(WORKDIR):/opt/app moviepy:latest /bin/bash