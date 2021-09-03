from pyfabdb.client import Client


class PyFabdb(Client):
    def __init__(self, url: str = 'https://api.fabdb.net', header: dict = {'Accept': 'application/json'}):
        super().__init__(url=url, header=header)

    def cards(self, page: int = 1, per_page: int = 25, keywords: str = '', pitch: str = '', cost: str = '', card_class: str = '', rarity: str = '', set: str = '') -> dict:
        ''' Get cards from fabdb API.
        :param page: When paginating through data sets, specifies the page.
            Integer.
        :param per_page: Specify the number of records per result set.
            Integer. Max-100
        :param keywords: A string representing a search term:
            String
        :params pitch: Search for a card with a given pitch.
            String. Valid values are: (1, 2, or 3)
        :params cost: Search for a card with a given cost.
            String. Valid values are: (1, 2, 3, or 4+)
        :params card_class: Search for a card that matches the required hero class.
           String. Valid values are: brute, guardian, mechanologist, ninja, ranger, runeblade, warrior, wizard.
        :params rarity: Search for a card that matches the specified rarity.
            String. Valid values are: C, R, S, T, L, F, P
        :params set: Search for cards from a given set.
            String. Valid values are: WTR, ARC, CRU, MON
        :return: A list of dictionaries with the cards' data.
        :rtype: dict{}

            Example Returned Data:
            {
                "current_page":19,
                "data": [
                    {
                        "identifier":"WTR219",
                        "name":"Nimblism",
                        "keywords":["generic","action"],
                        "stats":{"cost":"0","defense":"2","resource":"2"},
                    },
                    ...
                ],
                "first_page_url":"/cards?per_page=25&page=1",
                "from":451,
                "next_page_url":null,
                "path":"/cards",
                "per_page":"25",
                "prev_page_url":"/cards?per_page=25&page=18",
                "to":457
            }
        '''

        payload = {}

        if page:
            payload['page'] = page
        if per_page:
            payload['per_page'] = per_page
        if keywords:
            payload['keywords'] = keywords
        if pitch:
            payload['pitch'] = pitch
        if cost:
            payload['cost'] = cost
        if card_class:
            payload['class'] = card_class
        if rarity:
            payload['rarity'] = rarity
        if set:
            payload['set'] = set

        return self.get(path='/cards', params=payload)

    def get_card(self, id: str = 'absorb-in-aether-red') -> dict:
        ''' Get a card from fabdb API.
        :params id: The identifier of the card.
        :return: Returns a dictionary with the card's data.
        :rtype: dict
        '''
        payload = {}
        if id:
            payload['id'] = id

        return self.get(path=f'/cards/{id}', params=payload)

    def decks(self, slug: str = 'eLxddlzb') -> dict:
        ''' Get a deck from fabdb API.
        :params slug: The slug of the deck.
        :return: Returns a dictionary with the deck's data.
        :rtype: dict
        '''
        return self.get(path=f'/decks/{slug}')
