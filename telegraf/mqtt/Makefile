URI=http://localhost:8888/sources/0/chronograf/data-explorer?query=SELECT%20mean%28%22temperature%22%29%20AS%20%22mean_temperature%22%20FROM%20%22telegraf%22.%22autogen%22.%22influxmqtt_consumer%22%20WHERE%20time%20%3E%20%3AdashboardTime%3A%20GROUP%20BY%20time%28%3Ainterval%3A%29%2C%20%22host%22%20FILL%28null%29

up:
	@docker-compose up -d influxdb
	@sleep 2
	@docker-compose up -d
	@echo Sleeping for 20s to collect some data ...
	@sleep 20
	@xdg-open $(URI) || open $(URI) || echo "Open your browser to $(URI)"
	@docker-compose logs -f python telegraf

down:
	docker-compose down

clean:
	docker-compose down -v --rmi=local
