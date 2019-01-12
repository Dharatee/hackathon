from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 100)
    contact = models.BigIntegerField()
    address = models.CharField(max_length = 50)
    card_key = models.CharField(max_length = 16)
    blood_group = models.CharField(max_length = 3)
    user_type = models.CharField(max_length = 20)
    register_date = models.DateField()
    password = models.CharField(max_length = 20)
    is_new = models.BooleanField(default = True)
    def __str__(self):
        return self.name + ' - ' + self.card_key

class Transaction(models.Model):
    card_key = models.ForeignKey(User, on_delete=models.CASCADE)
    start = models.CharField(max_length = 20)
    end = models.CharField(max_length = 20)
    fare = models.PositiveSmallIntegerField()
    distance = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default = False)
    device_id = models.BigIntegerField()

    def __str__(self):
        return self.start

class Card(models.Model):
    card_key = models.ForeignKey(User, on_delete=models.CASCADE)
    expiry_date = models.DateField()
    created_date = models.DateField()
    balance = models.PositiveIntegerField()
    card_type = models.CharField(max_length = 20)

    def __str__(self):
        return self.card_type