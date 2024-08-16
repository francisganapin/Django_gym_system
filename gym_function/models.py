from django.db import models

class gym_members(models.Model):
    id_card = models.CharField(max_length=255, unique=True)
    expiry = models.DateField()
    membership = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    address = models.TextField()

    class Meta:
        db_table = 'gym_members'  # Name of the existing table WE use existing table we have last time

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
