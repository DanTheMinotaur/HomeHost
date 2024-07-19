# Backup Scripts

Files for creating backups with borg and uploading them to cloud storage provider. Set up as systemd jobs with timer for scheduling.

## systemctl commands 
```shell
sudo systemctl list-unit-files

sudo systemctl start borg_backup.service
sudo systemctl status borg_backup.service
sudo systemctl enable borg_backup.timer

sudo systemctl stop borg_backup.service
sudo systemctl disable borg_backup.timer

sudo systemctl enable remote_backup.timer
sudo systemctl status remote_backup.timer

# etc...
```