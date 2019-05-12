# Removing Tags with Kapacitor

```shell
docker-compose up -d

# Wait 10 minutes, so we have some "old" data that won't be caught by the stream task
docker-compose exec kapacitor /tmp/define-tasks.sh
```

This should clone all points from telegraf.autogen.cpu to telegraf.autogen.notag without the host tag

Live streaming handles new data in real-time with a stream task. Legacy data is handled by the batch job.

See `define-tasks.sh`
