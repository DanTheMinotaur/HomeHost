# HomeHost
A place for local apps and server configs

## Debian Installation

- Docker
- Python Ansible Modules

**Needs to be installed for docker ansible to work on remote**

```shell
pip install docker
pip install docker-compose
```

## deploy

```shell
# deploy all containers and scripts
./deploy.sh all

# deploy single container see docker_apps.yml
./deploy.sh Mosquitto
```

## Run Docker Install

```shell
# Deploy all containers
ansible-playbook docker.ansible.yml

# Deploy single container
ansible-playbook docker.ansible.yml --extra-vars 'single=Mosquitto'
```

## Setup server scripts

```shell
ansible-playbook scripts.ansible.yml --ask-become-pass
```
