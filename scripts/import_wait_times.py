#!/usr/bin/env python3

"""
Usage:
    ./import_wait_times.py {park ID}

GET https://queue-times.com/en-US/parks.json
for a list of parks and IDs
"""

import sys
from typing import Optional

from google_utils.bigquery import insert
from queue_time_utils.queue_times import get_park, get_queue_times


def main() -> None:
    if len(sys.argv) < 2:
        raise TypeError("Missing park ID argument")
    if len(sys.argv) > 2:
        raise TypeError("Too many arguments, expecting only park ID")

    park_id: int = int(sys.argv[1])
    queue_times: dict = get_queue_times(park_id)
    park: dict = get_park(park_id)

    rows = []

    def create_row(land_name: Optional[str], ride: dict) -> dict:
        return {
            "park": park["name"],
            "land": land_name,
            "ride": ride["name"],
            "is_open": ride["is_open"],
            "wait_time": ride["wait_time"],
            "last_updated": ride["last_updated"],
        }

    for land in queue_times["lands"]:
        for ride in land["rides"]:
            rows.append(create_row(land["name"], ride))

    for ride in queue_times["rides"]:
        rows.append(create_row(None, ride))

    insert("parks", "wait_times", rows)


if __name__ == "__main__":
    main()
