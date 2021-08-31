import json

from pyfab import pyfab

fab = pyfab.PyFab()


def test_cards():
    """Test the cards endpoint"""
    all_cards = fab.cards()
    print(fab.get_card())
    #print(json.dumps(all_cards, indent=4))
    assert isinstance(all_cards, dict)


def test_decks():
    """Test the decks endpoint"""
    decks = fab.decks(slug='qYyXnByL')
    print(decks)


test_cards()
test_decks()
