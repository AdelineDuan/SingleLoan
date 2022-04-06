from otree.api import *


class C(BaseConstants):
    # options = ("A", "B")
    endowment = cu(10)
    pass_gpa = [1, 0]


# pass_gpa = [1, 0]
# options = ("A", "B")


class Player(BasePlayer):
    # human_action = models.IntegerField(
    # choices=[
    #     [1, 'A'],
    #     [2, 'B']
    # ])
    human_action = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2])
    payoff = models.CurrencyField()


class Subsession(BaseSubsession):
    pass


# human_action = input('Which School will you choose? <A> or <B>?')
# human_action = human_action.upper()
# if human_action in actions:
#     print()

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

def school_choice_1(human_action):
    if human_action == 1:
        return [0.6, 0.4], [30, 40, 50, 60, 70], [0.1, 0.1, 0.3, 0.3, 0.2], 40

    elif human_action == 2:
        return [0.8, 0.2], [10, 20, 30, 40, 50], [0.2, 0.2, 0.2, 0.2, 0.2], 20


# payoff functions
def payoff_1(school_choice_1):
    pass_probs, salary_values, salary_probs, MSN = school_choice_1
    gpa = np.random.choice(C.pass_gpa, p=pass_probs)
    if gpa == 1:
        salary = np.random.choice(salary_values, p=salary_probs)
        Player.payoff = C.endowment + salary - MSN
    else:
        Player.payoff = 0


def payoff_2(school_choice_2):
    pass_probs, salary_values, salary_probs = school_choice_2
    gpa = np.random.choice(C.pass_gpa, p=pass_probs)
    if gpa == 1:
        salary = np.random.choice(salary_values, p=salary_probs)
        Player.payoff = C.endowment + salary
    else:
        Player.payoff = C.endowment


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


class Results(Page):
    pass


page_sequence = [Choice, Results]
