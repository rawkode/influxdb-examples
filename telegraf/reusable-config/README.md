# Telegraf - Reusable Config

If you need to share some common config between multiple Telegrafs, you can do so by specifying `--config-directory` and providing a directory with the shared `.conf` files.

In this case, we're going to configure both Telegrafs with system metric plugins and the same output, but each Telegraf also has its own `telegraf.conf`, which handles any unique configuration. In this example each `telegraf.conf` specifies a different interval and global tags.


```shell
# Telegraf 1
telegraf-1_1  | 2019-04-18T11:22:39Z I! Loaded outputs: influxdb
telegraf-1_1  | 2019-04-18T11:22:39Z I! Tags enabled: dc=telegraf-1 host=dd9f15494d82
telegraf-1_1  | 2019-04-18T11:22:39Z I! [agent] Config: Interval:10s, Quiet:false, Hostname:"dd9f15494d82", Flush Interval:10s

# Telegraf 2
telegraf-2_1  | 2019-04-18T11:22:39Z I! Loaded outputs: influxdb
telegraf-2_1  | 2019-04-18T11:22:39Z I! Tags enabled: dc=telegraf-2 host=26b25c34427b
telegraf-2_1  | 2019-04-18T11:22:39Z I! [agent] Config: Interval:5s, Quiet:false, Hostname:"26b25c34427b", Flush Interval:10s
```
