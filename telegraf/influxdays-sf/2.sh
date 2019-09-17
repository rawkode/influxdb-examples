#!/usr/bin/env sh
docker-compose exec influxdb2 influx setup --host http://localhost:9999 \
    -b influxdays \
    -o influxdata \
    -p influx123 \
    -u influx \
    -t influx \
    -f
