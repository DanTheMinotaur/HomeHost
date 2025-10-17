#!/bin/bash

TAR_PATH="/media/USB/SSD500GB/backups/.tar/unicorn.tar.gz"

# sudo setfacl -R -m u:$USER:rwx /home/daniel/.docker-volumes/

backup now
backup clean
backup archive $TAR_PATH

rclone copy $TAR_PATH GDrive:/Backups/Servers/borg --progress
