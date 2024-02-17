#!/bin/bash

# Tars a directory and uploads the generated file via Rclone
# Usage: upload_backup.sh /backup/borg/myfiles.repo //backups/

repos=${1:-$BORG_REPO_BACKUPS}
backup_remote_path=${2:-$BORG_REMOTE_PATH}

cd $repos

repos_list=$(ls -d1 */)

for r in $repos_list; do
    cd $repos && cd $r
    tar_dest="/tmp/$(basename $r).tar.gz"
    echo "Compressing $r"
    tar -czvf $tar_dest .
    echo "Uploading $tar_dest to $backup_remote_path"
    rclone --config $RCLONE_CONFIG copy $tar_dest "$BORG_RCLONE_GDRIVE:$backup_remote_path"
    echo "Upload finished"
    rm $tar_dest
done
