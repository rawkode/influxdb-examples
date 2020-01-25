influxdb:
	@docker container run --name influxdb --detach -p 9998:9999 --rm quay.io/influxdb/influxdb:2.0.0-beta

node:
	@docker container run --rm --link "influxdb:influxdb.com" -it --entrypoint=npm --volume $(shell pwd):/code --workdir /code --publish 3000:3000 node:11 start
