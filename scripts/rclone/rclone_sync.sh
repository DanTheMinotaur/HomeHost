#!/bin/bash
set -u 

rclone --config $RCLONE_CONFIG sync $1 "$RCLONE_GDRIVE:${2}" --transfers ${3:-30} --progress
