FROM python:3

# Install tools
RUN apt-get -y update && apt-get -y install ffmpeg imagemagick

# Install fonts
RUN apt-get -y install fonts-liberation

# Localization
RUN apt-get install -y locales \
    && locale-gen C.UTF-8 \
    && /usr/sbin/update-locale LANG=C.UTF-8

ENV LC_ALL C.UTF-8

# Install Python dependencies
COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app
RUN pip install -r requirements.txt

# modify ImageMagick policy file so that Textclips work correctly.
RUN sed -i 's/none/read,write/g' /etc/ImageMagick-6/policy.xml
