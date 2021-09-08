import pytest

from pyfabdb import pyfabdb


@pytest.fixture()
def fabdb():
    return pyfabdb.PyFabdb()


def test_get_card(fabdb):
    """ Test the get_card function """
    card = fabdb.get_card(id='absorb-in-aether-red')
    assert isinstance(card, dict)
    assert card['name'] == 'Absorb in Aether'
    assert card['type'] == 'defense'
    assert card['class'] == 'wizard'


def test_cards(fabdb):
    """ Test the cards function """
    cards = fabdb.cards()
    assert isinstance(cards, dict)
    assert len(cards['data']) > 0


def test_cards_by_pitch(fabdb):
    """ Test the cards function, param pitch """
    pitch_1 = fabdb.cards(pitch='1')
    assert isinstance(pitch_1, dict)
    assert len(pitch_1) > 0
    for card in pitch_1['data']:
        pitch = card['stats']['resource']
        assert pitch == '1' or pitch == 1

    pitch_2 = fabdb.cards(pitch='2')
    assert isinstance(pitch_2, dict)
    assert len(pitch_2) > 0
    for card in pitch_2['data']:
        pitch = card['stats']['resource']
        assert pitch == '2' or pitch == 2

    pitch_3 = fabdb.cards(pitch='3')
    assert isinstance(pitch_3, dict)
    assert len(pitch_3) > 0
    for card in pitch_3['data']:
        pitch = card['stats']['resource']
        assert pitch == '3' or pitch == 3

    # pitch can only be 1, 2, or 3
    pitch_4 = fabdb.cards(pitch='4')
    assert len(pitch_4['data']) == 0


def test_cards_by_keywords(fabdb):
    """ Test the cards function, param keywords"""
    keyword_1 = fabdb.cards(keywords='equipment')
    assert 'equipment' in keyword_1['data'][0]['keywords']


def test_cards_by_cost(fabdb):
    """ Test the cards function, param cost """
    cost_1 = fabdb.cards(cost='1')
    for card in cost_1['data']:
        cost = card['stats']['cost']
        assert cost == '1' or cost == 1

    cost_2 = fabdb.cards(cost='2')
    for card in cost_2['data']:
        cost = card['stats']['cost']
        assert cost == '2' or cost == 2

    cost_3 = fabdb.cards(cost='3')
    for card in cost_3['data']:
        cost = card['stats']['cost']
        assert cost == '3' or cost == 3

    # currently there is a bug with filtering for card with cost of 4
    # cost_4 = fabdb.cards(cost="4")
    # for card in cost_4["data"]:
    #     cost = card["stats"]["cost"]
    #     assert cost == "4" or cost == 4


def test_cards_by_rarity(fabdb):
    """ Test the cards function, param rarity """
    rarity_1 = fabdb.cards(rarity='C')
    # bug with rarity C, returns other rarity cards
    # for card in rarity_1["data"]:
    #     assert card["rarity"] == "C"
    assert len(rarity_1['data']) > 0

    rarity_2 = fabdb.cards(rarity='R')
    # bug with rarity R, returns other rarity cards
    # for card in rarity_2["data"]:
    #     assert card["rarity"] == "R"
    assert len(rarity_2['data']) > 0

    rarity_3 = fabdb.cards(rarity='S')
    for card in rarity_3['data']:
        assert card['rarity'] == 'S'
    assert len(rarity_3['data']) > 0

    rarity_4 = fabdb.cards(rarity='T')
    for card in rarity_4['data']:
        assert card['rarity'] == 'T'
    assert len(rarity_4['data']) > 0

    rarity_5 = fabdb.cards(rarity='L')
    for card in rarity_5['data']:
        assert card['rarity'] == 'L'
    assert len(rarity_5['data']) > 0

    rarity_6 = fabdb.cards(rarity='F')
    for card in rarity_6['data']:
        assert card['rarity'] == 'F'
    assert len(rarity_6['data']) > 0

    rarity_7 = fabdb.cards(rarity='P')
    # bug with rarity P, returns other rarity cards
    # for card in rarity_7["data"]:
    #     print(card["rarity"])
    # assert card["rarity"] == "P"
    assert len(rarity_7['data']) > 0


def test_cards_by_class(fabdb):
    """ Test the cards function, param card_class """
    brute = fabdb.cards(card_class='brute')
    assert len(brute['data']) > 0
    for cards in brute['data']:
        assert 'brute' in cards['keywords']

    guardian = fabdb.cards(card_class='guardian')
    assert len(guardian['data']) > 0
    for cards in guardian['data']:
        assert 'guardian' in cards['keywords']

    mechanologist = fabdb.cards(card_class='mechanologist')
    assert len(mechanologist['data']) > 0
    for cards in mechanologist['data']:
        assert 'mechanologist' in cards['keywords']

    ninja = fabdb.cards(card_class='ninja')
    assert len(ninja['data']) > 0
    for cards in ninja['data']:
        assert 'ninja' in cards['keywords']

    ranger = fabdb.cards(card_class='ranger')
    assert len(ranger['data']) > 0
    for cards in ranger['data']:
        assert 'ranger' in cards['keywords']

    runeblade = fabdb.cards(card_class='runeblade')
    assert len(runeblade['data']) > 0
    for cards in runeblade['data']:
        assert 'runeblade' in cards['keywords']

    warrior = fabdb.cards(card_class='warrior')
    assert len(warrior['data']) > 0
    for cards in warrior['data']:
        assert 'warrior' in cards['keywords']

    wizard = fabdb.cards(card_class='wizard')
    assert len(wizard['data']) > 0
    for cards in wizard['data']:
        assert 'wizard' in cards['keywords']


def test_cards_by_set(fabdb):
    """ Test the cards function, param set """
    wtr = fabdb.cards(set='WTR')
    assert len(wtr['data']) > 0

    arc = fabdb.cards(set='ARC')
    assert len(arc['data']) > 0

    cru = fabdb.cards(set='CRU')
    assert len(cru['data']) > 0

    mon = fabdb.cards(set='MON')
    assert len(mon['data']) > 0
