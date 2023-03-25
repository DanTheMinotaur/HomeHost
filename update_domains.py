#!/usr/bin/python3

import os
import yaml
import re
import sys

custom_list = 'apps/pihole/custom.list'

def get_compose_files():
    for root, _, files in os.walk("./apps"):
        for file in files:
            if file.endswith(".yml"):
                yield os.path.join(root, file)

def extract_domain(compose_path):
    with open(compose_path, 'r') as f:
        d_com: dict = yaml.safe_load(f)
    if 'services' not in d_com:
        return None 
    
    for s in d_com['services'].values():
        if 'labels' in s:
            for l in s['labels']:
                if 'traefik' in l and 'rule=Host' in l:
                    return re.search('\(`(.*)`\)', l).group(1)
    return None

if __name__ == "__main__":
    try:
        ip_addr = sys.argv[1]
    except IndexError:
        ip_addr = '192.168.0.2'

    domains = list(filter(None, [extract_domain(c) for c in get_compose_files()]))

    with open(custom_list, 'w') as f:
        for d in domains:
            f.write(f'{ip_addr} {d}\n')



             