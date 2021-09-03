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
