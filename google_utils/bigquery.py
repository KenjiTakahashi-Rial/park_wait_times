from typing import Union

from google.cloud.bigquery import Client
from google.cloud.bigquery.table import RowIterator, _EmptyRowIterator

CLIENT: Client = Client()


def query(query_str: str) -> Union[RowIterator, _EmptyRowIterator]:
    return CLIENT.query(query_str).result()
