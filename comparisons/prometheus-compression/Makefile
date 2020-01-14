setup: containers
	@docker-compose exec influxdb influx -import -path=/tmp/influxdb/ddl.txt
	@docker-compose exec influxdb2 influx setup -f --host 'http://localhost:9999' -b storagecomparison -o storagecomparison -p storagecomparison -u storagecomparison -t storagecomparison

containers:
	@docker-compose up -d
