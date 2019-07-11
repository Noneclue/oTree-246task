from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'six_task'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    answer = models.IntegerField(
        choices=[
            [1, "偶数の組み合わせである"],
            [2, "決まった数だけ増えていく数である"],
            [3, "中央の数は左右の数の平均である"],
            [4, "右の数は左より大きな数である"]
        ],
        widget=widgets.RadioSelect
    )
