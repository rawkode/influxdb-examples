#!/usr/bin/env sh
curl -i -XPOST 'http://localhost/write' -H "Host: telegraf.com" --data-binary 'cpu_load_short,host=server01,region=us-west value=0.64 1434055562000000000'
