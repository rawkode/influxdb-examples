# Storing Logs in InfluxDB

This setup will run:

- InfluxDB
- Telegraff (with syslog input plugin)
- Chronograf
- nginx

It configures the Docker Daemon to send nginx's logs to the Telegraf syslog listener. You could, instead, using fluentd to grab all the Docker container logs and ship to the same location.

Nginx will be available on http://localhost:8080
Chronograf will be available on http://localhost:8888

The more you hit Nginx, the more logs will show up in Chronograf.
