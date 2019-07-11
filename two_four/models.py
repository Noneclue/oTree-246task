from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'two_four'
    players_per_group = None
    num_rounds = 3

    true_say = "○：規則に合致しています"
    false_say = "×:規則に合致していません"


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    first_num = models.IntegerField(
        choices=list(range(10))
    )

    second_num = models.IntegerField(
        choices=list(range(10))
    )

    third_num = models.IntegerField(
        choices=list(range(10))
    )

    quit_loop = models.BooleanField()

    def truefalse(self):
        if self.first_num < self.second_num\
           and self.second_num < self.third_num:
            return Constants.true_say
        else:
            return Constants.false_say
