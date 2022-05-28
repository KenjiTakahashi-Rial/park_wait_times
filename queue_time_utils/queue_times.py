import json
from typing import Optional, Union

import requests

from func_utils.decorators import lazy_getter

PARKS_URL = "https://queue-times.com/en-US/parks.json"
QUEUE_TIMES_URL_TEMPLATE = (
    "https://queue-times.com/en-US/parks/{park_id}/queue_times.json"
)


# TODO: Create an exponential backoff retry decorator
def get_queue_times(park_id: int) -> dict:
    url: str = QUEUE_TIMES_URL_TEMPLATE.format(park_id=park_id)
    response: requests.Response = requests.get(url)
    return json.loads(response.text)


@lazy_getter
def get_parks() -> dict:
    response: requests.Response = requests.get(PARKS_URL)
    return json.loads(response.text)


def get_park(park_id: Union[int, str]) -> Optional[dict[str, Union[int, str]]]:
    park_id_int: int = int(park_id)
    for company in get_parks():
        for park in company["parks"]:
            if park["id"] == park_id_int:
                return park
    return None
