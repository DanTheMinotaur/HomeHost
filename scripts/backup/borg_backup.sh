#!/bin/bash

# Script to create and add a new borg backup entry and apply pruning rules
# Will generate a borg repo based on todays current date and remove any older rundendant ones
# Usage: borg_backup.sh /home/user/tobackup [predicate for archive]

to_backup=$1
backup_loc=$BORG_REPO_BACKUPS

host=${2:-$(hostname)}

date_str=$(date '+%Y%m%d')

repo_path="$backup_loc/${host}$(basename $to_backup).repo"

mkdir -p $repo_path

if [ ! -d "${repo_path}/config" ]; then
  borg init --encryption=repokey $repo_path
fi

borg create "${repo_path}::${date_str}" $to_backup

borg prune --keep-daily 3 --keep-weekly 4 --keep-monthly 12 --keep-last 1 $repo_path

borg compact $repo_path

echo $repo_path
