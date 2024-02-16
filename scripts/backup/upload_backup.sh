#!/bin/bash

# Tars a directory and uploads the generated file via Rclone
# Usage: upload_backup.sh /backup/borg/myfiles.repo //backups/

backup_repo=$1
backup_remote_loc=$2

tar_dest="/tmp/$(nasemame $backup_repo).tar.gz"

cd $backup_repo

tar -czvf $tar_dest . 

rclone --config $RCLONE_CONFIG copy $tar_dest "$BORG_RCLONE_GDRIVE:$backup_remote_loc"
