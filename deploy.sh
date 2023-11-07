#!/bin/bash

if [ -z "$1" ]; then
    echo "No arguments supplied"
    exit
fi

arg=$1
cmd="ansible-playbook docker.ansible.yml"

if [[ "$arg" != "all" ]] then
    cmd="$cmd --extra-vars 'single=$arg'"
fi

eval $cmd
