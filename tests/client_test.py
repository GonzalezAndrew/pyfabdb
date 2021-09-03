from pyfabdb.client import Client


def test_client():
    """Test client class"""
    header = {'Accept': 'application/json'}
    client = Client(header=header)
    assert client.header == header
    assert client.url == 'https://api.fabdb.net'
