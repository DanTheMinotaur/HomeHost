# danieldevine.dev prod deployer

This contains the docker compose files to deploy updates from https://github.com/DanTheMinotaur/danieldevine.dev/ repo. Running this will build any changes from the main repo. 

### $DOCKER_VOLUMES
Env var with directory for storing files from backend api. 

### $GITHUB_TOKEN_DDDEV
Needed to use GH token to clone the repo, encountered a bug with downloading over ssh when forwarding the agent. 

Create a Token with Repo read access and add it to server. 

