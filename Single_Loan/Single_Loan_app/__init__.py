from otree.api import *


doc = """
Single Loan
"""


class C(BaseConstants):
    NAME_IN_URL = 'Single_Loan_app'
    PLAYERS_PER_GROUP = 1
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]
