# Homer Dashboard

[Github](https://github.com/bastienwirtz/homer)

Dashboard is generated from [dashboard_gen.py](../../dashboard_gen.py) and generate the desired homer config and extract 
any matching icons it finds. 

## Config
The configuration is controlled from `dashboard_config` in [docker_apps.yml](../../data/docker_apps.yml). A docker container
to be added `docker_apps` for `dashboard_gen.py` to figure out where to extract the port number for routing.

New sections can be added to homer by adding a new key to `dashboard_config` and the docker container needs to be added to
its `apps` list. 

## Local/Remote
Two instances of Homer are set up to be able to use the dashboard depending o

## Icons
Icons sourced from: https://github.com/WalkxCode/dashboard-icons