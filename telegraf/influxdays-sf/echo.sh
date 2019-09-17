#!/usr/bin/env sh
echo "echo 512 | nc -q1 -U /tmp/telegraf.sock"
echo 512 | nc -q1 -U /tmp/telegraf.sock
