#!/usr/bin/env sh
echo curl -X POST http://localhost:8080/telegraf -d '{"name": "test", "some_value": 1, "some_other_value": 2}'
curl -X POST http://localhost:8080/telegraf -d '{"name": "test", "some_value": 1, "some_other_value": 2}'
echo curl -X POST http://localhost:8080/telegraf -d '{"name": "metric", "my_tag": "rawkode", "sum": 1}'
curl -X POST http://localhost:8080/telegraf -d '{"name": "metric", "my_tag": "rawkode", "sum": 1}'
