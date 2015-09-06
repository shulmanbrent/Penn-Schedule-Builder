FROM ubuntu:14.04
MAINTAINER Brent Shulman <shulmanbrent@yahoo.com>

RUN apt-get update

# Install development environment
RUN apt-get install --assume-yes python-dev
RUN apt-get install --assume-yes libhdf5-dev
RUN apt-get install --assume-yes python-pip
RUN apt-get install --assume-yes libpq-dev
RUN apt-get install --assume-yes wget
RUN apt-get install --assume-yes python-numpy
RUN apt-get install --assume-yes python-scipy
RUN apt-get install --assume-yes ipython
RUN apt-get install --assume-yes ipython-notebook
RUN apt-get install -y nano locales curl unzip openssl

# Install flask
RUN pip install flask
RUN pip install PennSDK

# Stage files in current folder in /data
ADD . /data

RUN pip install -r /data/requirements.txt

EXPOSE 8888
EXPOSE 5000
EXPOSE 80

# setup data volume
VOLUME ["/data"]

# default to shell
CMD ["python", "/data/application.py""]