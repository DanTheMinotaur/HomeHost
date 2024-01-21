#!/usr/bin/python

import yaml
import zipfile
from pathlib import Path
from difflib import get_close_matches

GENERAL_CONFIG = 'data/configs.yml'
DOCKER_APPS = 'data/docker_apps.yml'
HOMER_DIR = Path('apps/homer')
BASE_CONFIG = HOMER_DIR.joinpath('config_base.yml')
ICONS_DIR = HOMER_DIR.joinpath('icons/')
ICONS_ZIP = HOMER_DIR.joinpath('icons.zip')


def load_yaml_file(path: str or Path) -> dict:
    with open(path) as f:
        return yaml.safe_load(f)


def get_docker_port(compose_file: str or Path) -> int:
    services = load_yaml_file(compose_file)['services']
    ports = services[next(iter(services))]['ports']
    return ports[0].split(':')[0]


def find_icons(apps: list) -> dict[str, str]:
    icons_zip = [i.replace('.svg', '') for i in zipfile.ZipFile(ICONS_ZIP).namelist()]
    found_icons = {}
    for app in apps:
        try:
            found_icons[app] = str(get_close_matches(app, icons_zip)[0]) + '.svg'
        except IndexError:
            found_icons[app] = '__unknown.svg'
    return found_icons


def extract_icons(icons_to_extract: list, destination: Path) -> None:
    for icon in icons_to_extract:
        if not destination.joinpath(icon).is_file():
            zipfile.ZipFile(ICONS_ZIP).extract(icon, path=destination)


def generate_dashboard_services(base_url: str):
    docker_apps = load_yaml_file(DOCKER_APPS)
    dashboard_config: dict = docker_apps['dashboard_config']
    docker_app_configs: dict = docker_apps['docker_apps']
    homer_services = []
    for section, data in dashboard_config.items():
        service_group = {'name': section, 'icon': f'fas {data["icon"]}', 'items': []}

        apps = data['apps']
        icons = find_icons(list(apps.keys()))

        for name, desc in apps.items():
            port = get_docker_port(docker_app_configs[name]['compose_file'])
            service = {
                'name': name,
                'subtitle': desc,
                'url': f'{base_url}:{port}',
                'target': '_blank',
                'logo': f'assets/icons/{icons[name]}'
            }
            service_group['items'].append(service)
        extract_icons(list(icons.values()), ICONS_DIR)
        homer_services.append(service_group)

    return homer_services


def generate_homer_config(url_type: str, output_path: str or Path):
    base_config = load_yaml_file(BASE_CONFIG)
    generated = generate_dashboard_services(load_yaml_file(GENERAL_CONFIG)['global'][url_type])
    try:
        services = generated + base_config['services']
    except TypeError:
        services = generated

    base_config['services'] = services
    with open(output_path, 'w') as f:
        yaml.dump(base_config, f)


if __name__ == "__main__":
    generate_homer_config('dashboard_local', HOMER_DIR.joinpath('local/config.yml'))
    generate_homer_config('dashboard_vpn', HOMER_DIR.joinpath('remote/config.yml'))
