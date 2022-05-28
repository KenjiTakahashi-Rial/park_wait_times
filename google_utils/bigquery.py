from typing import Any, Union

from google.cloud.bigquery import Client
from google.cloud.bigquery.table import RowIterator, _EmptyRowIterator

CLIENT: Client = Client()


class InvalidInsertError(Exception):
    pass


def query(query_str: str) -> Union[RowIterator, _EmptyRowIterator]:
    return CLIENT.query(query_str).result()


def insert(dataset: str, table: str, rows: list[dict[str, Any]]) -> None:
    if not rows:
        return

    columns: list[str] = list(rows[0].keys())
    columns_str: str = f'({", ".join(columns)})'

    row_strs: list[str] = []

    for row in rows:
        value_strs: list[str] = []

        for value in row.values():
            value_str = str(value) if isinstance(value, int) else f'"""{str(value)}"""'
            value_strs.append(value_str)

        row_strs.append(f"({', '.join(value_strs)})")

    all_values_str: str = ",\n\t".join(row_strs)
    query_str: str = (
        f"INSERT INTO {dataset}.{table}\n"
        f"\t{columns_str}\n"
        f"VALUES\n"
        f"\t{all_values_str}"
    )
    query(query_str)
