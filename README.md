# HomeHost
A place for local apps and server configs

**Requires ansible**

Copy SSH Key

```shell
ssh-copy-id -i ~/.ssh/id_ed25519 dan@192.168.1.1
```

nix-install plugin
```shell
ansible-galaxy install danielrolls.nix
```

## Debian Installation

- Docker
- Python Ansible Modules

**Needs to be installed for docker ansible to work on remote**

```shell
pip install docker
pip install docker-compose
```

## Run Docker Install

```shell
ansible-playbook docker.ansible.yml
```

## Run Dev setup

```shell
ansible-playbook dev-setup.ansible.yml
```
