#!/bin/bash

if [ -z "$1" ]; then
    echo "No arguments supplied"
    exit
fi

arg=$1
cmd="ansible-playbook docker.ansible.yml"

./dashboard_gen.py

if [[ "$arg" != "all" ]] then
    cmd="$cmd --extra-vars 'single=$arg'"
fi

if [[ "$arg" == "Homer" ]] then
    cmd="$cmd --extra-vars 'single=HomerRemote' && $cmd --extra-vars 'single=HomerLocal'"
fi

eval $cmd
