from otree.api import *
from otree.models import player


class C(BaseConstants):
    endowment = 10
    pass_gpa = [1, 0]
    PLAYERS_PER_GROUP = None
    NAME_IN_URL = 'single_loan_trail'
    NUM_ROUNDS = 1
    MSN = 0


class Player(BasePlayer):
    human_action = models.IntegerField(widget=widgets.RadioSelect, choices=[[1, 'School A'], [2, 'School B']])

class Group(BaseGroup):
    pass


class Subsession(BaseSubsession):
    pass


# generate random discrete variable
import numpy as np


# import matplotlib.pyplot as plt

# # distribution of salary
# salary_values = [1, 2, 3, 4, 5, 6]
# salary_probs = [0.1, 0.1, 0.1, 0.1, 0.1, 0.5]
#
# # distribution of gpa

# pass_probs = [0.6, 0.4]
#
# # define MSN
# MSN = 40

# functions

# def school_choice_1(human_action):
#     if human_action == 1:
#         return [0.6, 0.4], [30, 40, 50, 60, 70], [0.1, 0.1, 0.3, 0.3, 0.2], 40
#
#     elif human_action == 2:
#         return [0.8, 0.2], [10, 20, 30, 40, 50], [0.2, 0.2, 0.2, 0.2, 0.2], 20


# result functions
def payoff_1(action):
    school_choice = -1
    if action == 1:
        school_choice = [0.6, 0.4], [30, 40, 50, 60, 70], [0.1, 0.1, 0.3, 0.3, 0.2], 40
    elif action == 2:
        school_choice = [0.8, 0.2], [10, 20, 30, 40, 50], [0.2, 0.2, 0.2, 0.2, 0.2], 20
    pass_probs, salary_values, salary_probs, MSN = school_choice
    gpa = np.random.choice(C.pass_gpa, p=pass_probs)
    if gpa == 1:
        salary = np.random.choice(salary_values, p=salary_probs)
        return C.endowment + salary - MSN
    else:
        return 0

def payoff_2(school_choice_2):
    pass_probs, salary_values, salary_probs = school_choice_2
    gpa = np.random.choice(C.pass_gpa, p=pass_probs)
    if gpa == 1:
    #    salary = models.CurrencyField(np.random.choice(salary_values, p=salary_probs))
        salary = cu(np.random.choice(salary_values, p=salary_probs))
        return C.endowment + salary
    else:
        return C.endowment


# result generating
# if human_action == 'A':
#     pass_probs = [0.6, 0.4]
#     salary_values = [30, 40, 50, 60, 70]
#     salary_probs = [0.1, 0.1, 0.3, 0.3, 0.2]
#     MSN = 40
#     print(payoff_1(C.endowment, pass_probs, salary_values, salary_probs, MSN))
# elif human_action == 'B':
#     pass_probs = [0.8, 0.2]
#     salary_values = [10, 20, 30, 40, 50]
#     salary_probs = [0.2, 0.2, 0.2, 0.2, 0.2]
#     MSN = 20
#     print(payoff_1(C.endowment, pass_probs, salary_values, salary_probs, MSN))
# else:
#     print('null')


# pages
class Choice(Page):
    form_model = 'player'
    form_fields = ['human_action']

    def before_next_page(player, timeout_happened):
        player.payoff = payoff_1(player.human_action)


class Results(Page):
    pass


page_sequence = [Choice, Results]
