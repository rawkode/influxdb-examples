# ISO8601 Date Formatting

## Telegraf Output

```shell
Starting iso8601_telegraf_1 ... done
Attaching to iso8601_telegraf_1
telegraf_1  | 2019-04-09T11:40:12Z I! Starting Telegraf 1.10.1
telegraf_1  | 2019-04-09T11:40:12Z I! Using config file: /etc/telegraf/telegraf.conf
telegraf_1  | 2019-04-09T11:40:13Z I! Loaded inputs: file
telegraf_1  | 2019-04-09T11:40:13Z I! Loaded aggregators:
telegraf_1  | 2019-04-09T11:40:13Z I! Loaded processors:
telegraf_1  | 2019-04-09T11:40:13Z I! Loaded outputs: file
telegraf_1  | 2019-04-09T11:40:13Z I! Tags enabled: host=9aff549622b9
telegraf_1  | 2019-04-09T11:40:13Z I! [agent] Config: Interval:10s, Quiet:false, Hostname:"9aff549622b9", Flush Interval:10s
telegraf_1  | 2019-04-09T11:40:13Z D! [agent] Connecting outputs
telegraf_1  | 2019-04-09T11:40:13Z D! [agent] Attempting connection to output: file
telegraf_1  | 2019-04-09T11:40:13Z D! [agent] Successfully connected to output: file
telegraf_1  | 2019-04-09T11:40:13Z D! [agent] Starting service inputs
telegraf_1  | 2019-04-09T11:40:29Z D! [outputs.file] wrote batch of 1 metrics in 386.4µs
telegraf_1  | 2019-04-09T11:40:29Z D! [outputs.file] buffer fullness: 0 / 10000 metrics.
telegraf_1  | file,author_username=rawkode,host=9aff549622b9,id=1773 comment_count=1,task_count=0 1552041178000000000
```
