import requests
from pprint import pprint

url="http://influxdb:9999/api/v2/query?org=rawkode"

headers = {
    "Authorization": "Token rawkode123",
    "Accept" : "application/csv",
    "Content-Type" : "application/vnd.flux"
}

data = """
from(bucket: "rawkode")
|> range(start: -2h)
"""

response = requests.post(url, headers=headers, data=data)

pprint(response.status_code)
pprint(response.text)
