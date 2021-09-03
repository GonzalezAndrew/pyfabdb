from pyfabdb.util import format_url


def test_format_url():
    """ Test the format_url utility function"""
    base_url = 'https://api.fabdb.net'
    path = '/cards'
    expected = base_url + path
    assert format_url(base_url, path) == expected
