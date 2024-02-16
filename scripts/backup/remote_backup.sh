#!/bin/bash

# Simple script to mount remote filesystem and backup using existing borg backup flow
# Usage: remote_backup.sh user 192.168.0.1 /home/user/project 

user=$1
remote=$2
to_backup=$3
repo_loc=$BORG_REPO_BACKUPS

sshstr="$user@$remote"

hostname=$(ssh $sshstr -f 'hostname')

mounted="/mnt/$(basename $to_backup)"

mkdir -p $mounted

sshfs -o allow_other,default_permissions $sshstr:$to_backup $mounted

repo_path=$(/usr/local/bin/borg_backup.sh $mounted $hostname)

umount $mounted

echo $repo_path