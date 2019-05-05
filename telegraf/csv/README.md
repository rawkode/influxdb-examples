# CSV Parsing with Tail Input

Uses `tail` input plugin, instead of `file`, so that the entire file isn't processed every `interval`.

Commented out timestamp examples from (https://www.reddit.com/r/influxdb/comments/bkttj8/requesting_help_only_first_line_from_csv_file_is/), as I don't think it can be parsed in such a weak format.

## Output

```
> select * from tail
name: tail
time                ComputerName Id    IsOpen ProcessName           Time              UserName host         path
----                ------------ --    ------ -----------           ----              -------- ----         ----
1557087344019300200 Computer1    11524 1      Adobe Desktop Service 3.5.2019 12.17.00 User1    ee9ef3e20439 /data/data.csv
1557087344019398000 Computer2    11524 0      Adobe Desktop Service 3.5.2019 14.17.59 User1    ee9ef3e20439 /data/data.csv
1557087344019467500 Computer3    11524 0      Adobe Desktop Service 3.5.2019 14.17.59 User1    ee9ef3e20439 /data/data.csv
1557087344019550100 Computer4    11524 0      Adobe Desktop Service 3.5.2019 14.17.59 User1    ee9ef3e20439 /data/data.csv
1557087344019584100 Computer5    11524 0      Adobe Desktop Service 3.5.2019 14.17.59 User1    ee9ef3e20439 /data/data.csv
```
