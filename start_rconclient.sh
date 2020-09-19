#!/bin/bash

# Start the factorio rcon client
# If the 1st argument is given, then HOSTNAME will be set with 1st argument
# If the 2nd argument is given, then PORT will be set with 2nd argument


if [ "$#" -ge 1 ]; then
    ENVS="--env HOSTNAME=$1"
fi

if [ "$#" -ge 2 ]; then
    ENVS="$ENVS --env PORT=$2"
fi

docker run -ti --rm \
  $ENVS \
  --name rconclient denmor/factorio-rcon-client:latest
