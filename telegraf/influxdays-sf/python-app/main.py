from flask import Flask
from influxdb import InfluxDBClient
from time import sleep
app = Flask(__name__)

cache = {'requests': 0}


@app.route("/")
def hello():
    client = InfluxDBClient(host='telegraf-edge', port=8086)

    sleep(cache['requests'])
    cache['requests'] = cache['requests'] + 1

    points = [
        {
            "measurement": "web-metrics",
            "tags": {
                "user": "anonymous",
                "endpoint": "hello"
            },
            "fields": {
                "response_time": cache['requests'],
                "total_requests": cache['requests']
            }
        },
    ]
    client.write_points(points)

    return "Response Time was " + str(cache['requests']) + " seconds"


if __name__ == "__main__":
    app.run()
