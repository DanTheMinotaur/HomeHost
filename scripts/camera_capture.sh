#!/bin/bash

pth="${CAMERA_IMAGE_DIR}$(date '+%Y%m%d')/"

mkdir -p $pth

ffmpeg -y -i $1 -rtsp_transport tcp -vframes 1 "${pth}$(date '+%Y%m%d%H%M%S').jpg"
