from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Instruction(Page):
    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        self.participant.vars["quit"] = False


class Guess(Page):
    def is_displayed(self):
        return not self.participant.vars["quit"]

    form_model = models.Player
    form_fields = ["first_num", "second_num", "third_num"]


class Results(Page):
    def is_displayed(self):
        return not self.participant.vars["quit"]

    form_model = models.Player
    form_fields = ["quit_loop"]

    def before_next_page(self):
        if self.player.quit_loop:
            self.participant.vars["quit"] = True
        else:
            self.participant.vars["quit"] = False


page_sequence = [
    Instruction,
    Guess,
    Results
]
