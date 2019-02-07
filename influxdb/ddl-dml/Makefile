.DEFAULT_GOAL := default

default: up load open

up:
	@docker-compose up -d

load:
	@echo Loading DDL
	@docker-compose exec influxdb influx -import -path=/tmp/ddl.txt
	@echo Loading DML
	@docker-compose exec influxdb influx -import -path=/tmp/dml.txt
	@echo Loading DDL+DML from together.txt
	@docker-compose exec influxdb influx -import -path=/tmp/together.txt

open:
	@xdg-open http://localhost:8888 || open http://localhost:8888 || echo "Open http://localhost:888"

clean:
	@docker-compose down -v
