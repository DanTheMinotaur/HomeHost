#!/bin/bash

HDD_DIR="/media/USB/hdd1"
TV_TEMPLATE='{{ .Name }}/{{ .Name }} Season {{ printf "%02d" .Season }}/Episode {{ printf "%02d" .Episode }}{{ if ne .ExtraEpisode -1 }}-{{ printf "%02d" .ExtraEpisode }}{{end}}.{{ .Ext }}'

media-sort \
--tv-dir "${HDD_DIR}/TV" \
--movie-dir "${HDD_DIR}/Movies" \
--recursive \
--action link \
--tv-template "${TV_TEMPLATE}" \
--file-limit 20000 \
--hard-link \
"${HDD_DIR}/Downloads"
