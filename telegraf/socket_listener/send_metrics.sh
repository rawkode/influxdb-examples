#!/usr/bin/env bash
while :;
do
    echo "measurement_name,city=Glasgow some_value=1i,another_value=2i" | nc -w 1 -u telegraf 8125;
    sleep 1;
done
