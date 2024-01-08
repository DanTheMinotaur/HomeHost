# Ansible repeatable tasks

## docker-compose-deploy.yml

A highly generic docker deployment task, which copies various files and setups for differnet docker configs, after 
it will run the container from `compose_file`. 

### Usage 

```yaml

tasks:
    - include_task: ansible/tasks/docker-compose-deploy.yml
    vars:
        app_name: "HomeAssistant" # Name of dir that files are copied to. 
        compose_file: "homeassistant/docker-compose.yml" # Name of compose file
        files: # Config files to be copied, jinja syntax will be rendered  
            - homeassistant/config.yml
        dirs: # Creates empty directories that may be needed
            - tmp
        bins: # Copies files "as-is" that don't need template rendering
            - homeassistant/backup.tar.gz

```
