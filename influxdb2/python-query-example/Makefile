dshell:
	@docker-compose run --rm --service-ports --entrypoint=ash python

setup:
	@curl -XPOST \
		-H "Content-type: application/json" \
		-d '{"username": "rawkode", "token": "rawkode123", "password": "rawkode123", "org": "rawkode", "bucket": "rawkode", "retentionPeriodHrs": 0 }' \
		http://influxdb:9999/api/v2/setup

load-data:
	@curl -XPOST \
		-H "Authorization: Token rawkode123" \
		-d 'measurement,name=rawkode random=457373' \
		"http://influxdb:9999/api/v2/write?org=rawkode&bucket=rawkode"
