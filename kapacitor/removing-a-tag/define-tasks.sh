#!/usr/bin/env bash
kapacitor define notag-stream -tick /tmp/live-stream.tick
kapacitor enable notag-stream
kapacitor define notag-batch -tick /tmp/historical-batch.tick
kapacitor replay-live batch -task notag-batch -past 90d -rec-time
