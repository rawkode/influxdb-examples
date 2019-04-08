.DEFAULT_GOAL := default

default: up load open

up:
	@docker-compose up -d

load:
	@echo Loading DDL
	@docker-compose exec influxdb influx -import -path=/tmp/ddl.txt
	@echo Loading Continuous Query
	@docker-compose exec influxdb bash -c "cat /tmp/cq.txt | influx -database system_stats"

open:
	@xdg-open http://localhost:8888 || open http://localhost:8888 || echo "Open http://localhost:888"

clean:
	@docker-compose down -v
