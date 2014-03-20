from django.db import models
from datetime import date
from utils.constants import EnumDecimalDigits


class Restaurant(models.Model):

    name = models.CharField(verbose_name='Name', max_length=100)


class Meal(models.Model):

    price = models.DecimalField(
        verbose_name='Price', max_digits=EnumDecimalDigits.max_digits, decimal_places=EnumDecimalDigits.decimal_places
    )
    date = models.DateField(verbose_name='Date', auto_now=True)


class Card(models.Model):

    balance = models.DecimalField(
        verbose_name='Balance', max_digits=EnumDecimalDigits.max_digits, decimal_places=EnumDecimalDigits.decimal_places
    )
    recharge_date = models.DateField(verbose_name='Recharge Date', auto_now=True, default=date.today())