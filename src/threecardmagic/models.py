from django.db import models
from django.conf import settings


class League(models.Model):
    name = models.TextField("League Name", blank=False, null=False)
    rulestext = models.TextField("League Rules", blank=False, null=False)
    active = models.BooleanField("Current League", default=False)


class Round(models.Model):
    league = models.ForeignKey(League)
    winner = models.ForeignKey(settings.AUTH_USER_MODEL)
    active = models.BooleanField("Current League", default=False)


class Card(models.Model):
    name = models.TextField("Card Name", blank=False, null=False)
    oracle_text = models.TextField("Card Oracle text", blank=False, null=False)
    image_link = models.TextField("Gatherer Image Link", blank=False, null=False)


class Deck(models.Model):
    name = models.TextField("Card Name", blank=True, null=False)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL)
    cards = models.ManyToManyField(Card)


class Match(models.Model):
    round_id = models.ForeignKey(Round)
    decks = models.ManyToManyField(Deck)


class Decision(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    match = models.ForeignKey(Match)
    comment = models.TextField("Justification", blank=False, null=False)
    score = models.CharField("Score X-Y", max_length=3)

