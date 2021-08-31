from pyfab import pyfab

fab = pyfab.PyFab()


def test_cards():
    """Test the cards endpoint"""
    all_cards = fab.cards()
    assert isinstance(all_cards, dict)


def test_decks():
    """Test the decks endpoint"""
    decks = fab.decks(slug='qYyXnByL')
    assert isinstance(decks, dict)


test_cards()
test_decks()
