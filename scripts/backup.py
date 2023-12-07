#!/usr/bin/python
import subprocess
from datetime import date
import sys
from os import path, environ, remove

REPO_HOME = "/backups/"

"""
Simple script to backup chosen directory using borg https://www.borgbackup.org/ and sync to Google Drive using rclone.
The script will name the backup `basename(path).repo`, it's only made to make a daily backup using YYYYMMDD as the 
repo key. 

Usage:

./backup.py /home/daniel/Devel

Requires BORG_RCLONE_GDRIVE, BORG_PASSPHRASE env variables to be set. 
"""


def run(cmd, **kwargs):
    print(cmd)
    subprocess.run(cmd, shell=True, **kwargs)


def borg(cmd):
    run(f'borg {cmd}')


def repo_init(repo_path):
    borg(f'init --encryption=repokey {repo_path}')


def repo_create(repo_path, repo_entry, files):
    borg(f'create {repo_path}::{repo_entry} {files}')


def rclone(cmd):
    run(f"rclone --config {environ['RCLONE_CONFIG']} {cmd}")


def tar(path_to_zip, dest_archive):
    run(f'tar -czvf {dest_archive} .', cwd=path_to_zip)


def rclone_copy(repo_path):
    remote_loc = environ['BORG_RCLONE_GDRIVE']
    rclone(f'copy {repo_path} {remote_loc}')


def main():
    backup = list(sys.argv)[1]
    if not len(backup):
        print('No backup specified')
        exit()

    repo_path = path.join(REPO_HOME, path.basename(backup).strip('.') + '.repo')

    if not path.isdir(repo_path):
        print(f'Creating repo {repo_path}')
        repo_init(repo_path)

    repo_entry = date.today().strftime("%Y%m%d")

    repo_create(repo_path, repo_entry, backup)

    archive_path = f'/tmp/{path.basename(repo_path)}.tar.gz'

    tar(repo_path, archive_path)

    rclone_copy(archive_path)

    if path.exists(archive_path):
        remove(archive_path)


if __name__ == "__main__":
    main()