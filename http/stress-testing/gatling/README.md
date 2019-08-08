# Gatling Metrics

**Gatling currently isn't sending metrics to Telegraf**

## InfluxDB through Telegraf

This demo using Telegraf as a Graphite endpoint, rather than InfluxDB directly, to emulate writing to InfluxCloud v1.

## Running

```shell
make up

# Follow interactive prompts
# Then open browser to http://localhost:8888 and explore the telegraf database
```
