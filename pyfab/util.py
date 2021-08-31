import csv
import io
from typing import List


def format_url(base_url: str, path: str) -> str:
    """
    Helper function to format a URL.
    :param base_url: The base URL.
    :param path: The path to append to the base URL.
    :return: The formatted URL.
    :rtype: str
    """
    if base_url is None or path is None:
        raise ValueError('base_url or path must be set')

    if base_url.endswith('/'):
        base_url = base_url.rstrip('/')

    if not path.startswith('/'):
        path = '/' + path

    if path.endswith('/'):
        path = path.rstrip('/')

    return base_url + path


def csv_to_json(data: csv.DictReader) -> List:
    """
    might not need this, gotta test csv output from fab api
    """
    return_list = []

    if not isinstance(data, csv.DictReader):
        data = csv.DictReader(io.StringIO(data))

    for row in data:
        return_list.append(dict(row))

    return return_list
