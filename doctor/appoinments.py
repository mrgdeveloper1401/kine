CARD_SESSSION_ID = 'card'


class Appoinments:
    def __init__(self, request):
        self.session = request.session
        card = self.session.get(CARD_SESSSION_ID)
        if card is None:
            card = self.session[CARD_SESSSION_ID] = {}
        self.card = card