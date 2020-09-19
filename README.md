README to Factorio RCON Client
===

This is a docker repository for a rcon client, based on factorio-rcon-py (see https://pypi.org/project/factorio-rcon-py/)


# Environment variables

|Available variables      |Description                                                |
|-------------------------|-----------------------------------------------------------|
|`HOSTNAME`              | The hostname of the factorio server            |
|`PORT`              | The RCON port of the factorio server           |

# Start the console

Use the script `start_rconclient.sh`:
```console
./start_rconclient.sh [hostname [port]]
```

It is possible to start also directly the console using the command `docker run`:
```console
docker run -ti --rm \
  [--env HOSTNAME=<hostname> \ ]
  [--env PORT=<port> \ ]
  --name rconclient denmor/factorio-rcon-client:latest
```
or

```console
docker run -ti --rm \
  --name rconclient denmor/factorio-rcon-client:latest \
  python rcon_client.py [hostname [port]]
```


# Make user admin

It is possible to promote directly a user as administrator using the command:
```console
docker run -ti --rm \
  --name rconclient denmor/factorio-rcon-client:latest \
  python make_admin.py [hostname [port]]
```

# License

The repository itself is under MIT licence. (see [LICENSE](./LICENSE))
