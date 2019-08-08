up:
	@docker-compose up -d chronograf influxdb telegraf
	@docker-compose run --rm --entrypoint=gatling.sh gatling
