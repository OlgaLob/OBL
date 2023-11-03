from django.db import models


class Company(models.Model):
    name = models.Model(max_length=100, blank=False, null=False)
    INN = models.CharField(max_length=12)
    is_holding_garnizon = models.BooleanField(default=False)
    is_group_OBL = models.BooleanField(default=False)


class Currency(models.Model):
    name = models.CharField(max_length=4)
    exchange_rate = models.DecimalField(max_digits=8, decimal_places=4)


class Account(models.Model):
    num_account = models.CharField(max_length=10)
    name_account = models.CharField(max_length=100)


class AccountingEntries(models.Model):
    doc_number = models.IntegerField(blank=False, null=False)
    create_at = models.DateTimeField(auto_now_add=False, blank=False, null=False)
    specification = models.CharField(blank=True, null=True)
    doc_name = models.CharField(max_length=150)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    account_dt = models.ForeignKey(Account, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=10)
    quantity_dt = models.DecimalField(max_digits=15, decimal_places=3)
    currency_dt = models.ForeignKey(Currency, on_delete=models.CASCADE)
    value_in_currency_dt = models.DecimalField(max_digits=15, decimal_places=2)
