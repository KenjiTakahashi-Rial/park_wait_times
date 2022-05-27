import json

import requests

URL_TEMPLATE = "https://queue-times.com/en-US/parks/{park_id}/queue_times.json"


# TODO: Create an exponential backoff retry decorator
def get_queue_times(park_id: int) -> dict:
    url: str = URL_TEMPLATE.format(park_id=park_id)
    response: requests.Response = requests.get(url)
    return json.loads(response.text)
