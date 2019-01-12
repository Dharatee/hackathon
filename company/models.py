from django.db import models

class Company(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length = 50)
    email = models.CharField(max_length = 100)
    contact = models.BigIntegerField()
    password = models.CharField(max_length = 20)
    company_name = models.CharField(max_length=50)
    bus_no = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.company_name

class Device(models.Model):
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    vehicle_no = models.PositiveSmallIntegerField()
    enter_device_id = models.CharField(max_length = 20)
    exit_device_id = models.CharField(max_length = 20)
    balance = models.PositiveSmallIntegerField()
    owner = models.CharField(max_length = 20)

    def __str__(self):
        return self.owner
