FROM rawkode/telegraf:byo AS build

FROM alpine:3.7 AS telegraf

COPY --from=build /etc/telegraf /etc/telegraf
COPY --from=build /go/src/github.com/influxdata/telegraf/telegraf /bin/telegraf
ENTRYPOINT [ "/bin/telegraf" ]
