2019-11_dht22.csv:
	@curl http://archive.luftdaten.info/csv_per_month/2019-11/2019-11_dht22.zip -o 2019-11_dht22.zip
	@unzip 2019-11_dht22.zip

setup: 2019-11_dht22.csv
	@docker-compose up -d influxdb
	@sleep 10
	@docker-compose exec influxdb influx setup -f --host 'http://localhost:9999' -b luftdaten -o luftdaten -p luftdaten123 -u luftdaten -t luftdaten

import:
	@docker-compose run --rm telegraf

clean:
	@docker-compose down -v