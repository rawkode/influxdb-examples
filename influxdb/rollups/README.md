# InfluxDB Rollup Example

This example will use InfluxDB's Continuous Queries to rollup data from 1s resolution to 1h resolution.

## DDL

This describes our database and retention policies.

## Continuous Query

The `RESAMPLE EVERY 1m` is **not** needed. This is only provided so you can begin to see rolled up data within a short period of time.

## Telegraf

Telegraf is writing metrics with a 1s interval, into our `twoweek` retention policy.
