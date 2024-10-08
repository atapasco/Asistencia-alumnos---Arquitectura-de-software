#!/bin/bash
host="$1"
shift
port="$1"
shift
until nc -z "$host" "$port"; do
    echo "Waiting for $host:$port..."
    sleep 1
done
sleep 6
exec "$@"