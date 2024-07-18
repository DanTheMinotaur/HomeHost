#!/bin/bash

ffmpeg -y -i $1 -rtsp_transport tcp -vframes 1 "${CAMERA_IMAGE_DIR}$(date '+%Y%m%d%H%M%S').jpg"
