setup:
	@git clone https://github.com/influxdata/influxdb-jsonnet

influxdb:
	@docker container run --detach --rm --publish 9999:9999 quay.io/influxdb/influxdb:2.0.0-beta

influxdb-setup:
	@influx setup --force -u rawkode -p rawkode123 -t rawkode -o rawkode -b rawkode -r 0

compile:
	@jsonnet -J ./influxdb-jsonnet ./src/main.jsonnet
