import pytest

from pyfabdb import pyfabdb


@pytest.fixture()
def fabdb():
    return pyfabdb.PyFabdb()


def test_decks(fabdb):
    """ Test decks function"""
    deck = fabdb.decks(slug='eLxddlzb')
    assert deck['name'] == 'Official Rhinar Hero Deck'
    assert deck['format'] == 'constructed'
    assert len(deck['cards']) > 0
