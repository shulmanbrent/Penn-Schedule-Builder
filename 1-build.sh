#!/bin/bash

# image name
__image=shulmanbrent/penn-scheduler-flask

# build image
docker build -t $__image .