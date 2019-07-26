# Writing to Elasticsearch

This is an example of writing to Elasticsearch through Telegraf's InfluxDB interface

## How

First, we have `telegraf`, which grabs system metrics and writes them to "InfluxDB". This InfluxDB (`telegraf-influxdb`) is actually a Telegraf with the `influxdb_listener` input plugin. It is configured with the Elasticsearch output plugin.

## Output

```
{
  "took": 7,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 108,
      "relation": "eq"
    },
    "max_score": 1.0,
    "hits": [{
      "_index": "telegraf-2019.07.26",
      "_type": "metrics",
      "_id": "U_2TLmwBFoL6bVdC51s6",
      "_score": 1.0,
      "_source": {
        "@timestamp": "2019-07-26T13:58:30Z",
        "measurement_name": "system",
        "system": {
          "load1": 2.25,
          "load15": 0.81,
          "load5": 1.47,
          "n_cpus": 8,
          "n_users": 0
        },
        "tag": {
          "host": "90e78c26e1ff"
        }
      }
    }, {
      "_index": "telegraf-2019.07.26",
      "_type": "metrics",
      "_id": "VP2TLmwBFoL6bVdC51s6",
      "_score": 1.0,
      "_source": {
        "@timestamp": "2019-07-26T13:58:30Z",
        "measurement_name": "mem",
        "mem": {
          "active": 5002346496,
          "available": 11002675200,
          "available_percent": 66.57207823991178,
          "buffered": 5427200,
          "cached": 4386349056,
          "commit_limit": 29737512960,
          "committed_as": 14315175936,
          "dirty": 2134016,
          "free": 7185682432,
          "high_free": 0,
          "high_total": 0,
          "huge_page_size": 2097152,
          "huge_pages_free": 0,
          "huge_pages_total": 0,
          "inactive": 3392323584,
          "low_free": 0,
          "low_total": 0,
          "mapped": 934068224,
          "page_tables": 48852992,
          "shared": 703135744,
          "slab": 234184704,
          "swap_cached": 0,
          "swap_free": 21473783808,
          "swap_total": 21473783808,
          "total": 16527462400,
          "used": 4950003712,
          "used_percent": 29.950173790744792,
          "vmalloc_chunk": 0,
          "vmalloc_total": 35184372087808,
          "vmalloc_used": 0,
          "wired": 0,
          "write_back": 0,
          "write_back_tmp": 0
        },
        "tag": {
          "host": "90e78c26e1ff"
        }
      }
    }, {
      "_index": "telegraf-2019.07.26",
      "_type": "metrics",
      "_id": "Vf2TLmwBFoL6bVdC51s6",
      "_score": 1.0,
      "_source": {
        "@timestamp": "2019-07-26T13:58:30Z",
        "measurement_name": "system",
        "system": {
          "uptime": 759
        },
        "tag": {
          "host": "90e78c26e1ff"
        }
      }
    }, {
      "_index": "telegraf-2019.07.26",
      "_type": "metrics",
      "_id": "Vv2TLmwBFoL6bVdC51s6",
      "_score": 1.0,
      "_source": {
        "@timestamp": "2019-07-26T13:58:30Z",
        "measurement_name": "system",
        "system": {
          "uptime_format": " 0:12"
        },
        "tag": {
          "host": "90e78c26e1ff"
        }
      }
    }, {
      "_index": "telegraf-2019.07.26",
      "_type": "metrics",
      "_id": "V_2TLmwBFoL6bVdC51s6",
      "_score": 1.0,
      "_source": {
        "@timestamp": "2019-07-26T13:58:40Z",
        "measurement_name": "system",
        "system": {
          "load1": 2.38,
          "load15": 0.84,
          "load5": 1.52,
          "n_cpus": 8,
          "n_users": 0
        },
        "tag": {
          "host": "90e78c26e1ff"
        }
      }
    }, {
      "_index": "telegraf-2019.07.26",
      "_type": "metrics",
      "_id": "WP2TLmwBFoL6bVdC51s6",
      "_score": 1.0,
      "_source": {
        "@timestamp": "2019-07-26T13:58:40Z",
        "measurement_name": "system",
        "system": {
          "uptime": 769
        },
        "tag": {
          "host": "90e78c26e1ff"
        }
      }
    }, {
      "_index": "telegraf-2019.07.26",
      "_type": "metrics",
      "_id": "Wf2TLmwBFoL6bVdC51s6",
      "_score": 1.0,
      "_source": {
        "@timestamp": "2019-07-26T13:58:40Z",
        "measurement_name": "mem",
        "mem": {
          "active": 4995919872,
          "available": 10993901568,
          "available_percent": 66.51899306695745,
          "buffered": 5427200,
          "cached": 4402786304,
          "commit_limit": 29737512960,
          "committed_as": 14332747776,
          "dirty": 2400256,
          "free": 7176032256,
          "high_free": 0,
          "high_total": 0,
          "huge_page_size": 2097152,
          "huge_pages_free": 0,
          "huge_pages_total": 0,
          "inactive": 3394998272,
          "low_free": 0,
          "low_total": 0,
          "mapped": 936611840,
          "page_tables": 48844800,
          "shared": 718831616,
          "slab": 231620608,
          "swap_cached": 0,
          "swap_free": 21473783808,
          "swap_total": 21473783808,
          "total": 16527462400,
          "used": 4943216640,
          "used_percent": 29.90910836983662,
          "vmalloc_chunk": 0,
          "vmalloc_total": 35184372087808,
          "vmalloc_used": 0,
          "wired": 0,
          "write_back": 0,
          "write_back_tmp": 0
        },
        "tag": {
          "host": "90e78c26e1ff"
        }
      }
    }, {
      "_index": "telegraf-2019.07.26",
      "_type": "metrics",
      "_id": "Wv2TLmwBFoL6bVdC51s6",
      "_score": 1.0,
      "_source": {
        "@timestamp": "2019-07-26T13:58:40Z",
        "measurement_name": "system",
        "system": {
          "uptime_format": " 0:12"
        },
        "tag": {
          "host": "90e78c26e1ff"
        }
      }
    }, {
      "_index": "telegraf-2019.07.26",
      "_type": "metrics",
      "_id": "W_2TLmwBFoL6bVdC51s6",
      "_score": 1.0,
      "_source": {
        "@timestamp": "2019-07-26T13:58:40Z",
        "cpu": {
          "usage_guest": 0,
          "usage_guest_nice": 0,
          "usage_idle": 90.73705179282813,
          "usage_iowait": 0.298804780876492,
          "usage_irq": 0,
          "usage_nice": 0,
          "usage_softirq": 1.394422310756967,
          "usage_steal": 0,
          "usage_system": 1.6932270916334702,
          "usage_user": 5.876494023904371
        },
        "measurement_name": "cpu",
        "tag": {
          "cpu": "cpu0",
          "host": "90e78c26e1ff"
        }
      }
    }, {
      "_index": "telegraf-2019.07.26",
      "_type": "metrics",
      "_id": "XP2TLmwBFoL6bVdC51s6",
      "_score": 1.0,
      "_source": {
        "@timestamp": "2019-07-26T13:58:40Z",
        "cpu": {
          "usage_guest": 0,
          "usage_guest_nice": 0,
          "usage_idle": 88.5973763874874,
          "usage_iowait": 0.4036326942482358,
          "usage_irq": 0,
          "usage_nice": 0,
          "usage_softirq": 0.30272452068617905,
          "usage_steal": 0,
          "usage_system": 1.9172552976790953,
          "usage_user": 8.779011099899165
        },
        "measurement_name": "cpu",
        "tag": {
          "cpu": "cpu1",
          "host": "90e78c26e1ff"
        }
      }
    }]
  }
}
```
