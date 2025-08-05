# Adguard Home setup

> Need to change the default webui port in `AdGuardHome.yaml` for reverse proxy

## API Usage

https://github.com/AdguardTeam/AdGuardHome/blob/master/openapi/README.md 

Creating Bearer

```shell
echo -n 'myuser:password' | base64
```

```sh
curl -X 'GET' \
  'http://localhost/control/clients' \
  -H 'accept: application/json' \
  -H 'Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ='
```