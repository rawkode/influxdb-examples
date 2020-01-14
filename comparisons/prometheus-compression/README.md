# Compression Comparison

This directory has some code to test the compression of InfluxDB with Prometheus.

## Setup

### Configure InfluxDB

InfluxDB has been configured to use a retention policy of 15d, and a shard duration of 2 hours

## Notes

- Prometheus retention is 15d, but this can be configured
- Prometheus shard duration is 2 hours and cannot be changed
- InfluxDB's shard duration is changes depending on the retention policy duration
  - Default retention is forever, which has a shard duration of 1w
  - Retention policy durations less than 2 days means a shard duration of 1h
  - Retention policy durations longer than 2 days, but less than 6 months, means a shard duration of 1d
