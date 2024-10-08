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



class gym_item(models.Model):
        item_name = models.CharField(max_length=255)
        stock = models.IntegerField()
        description = models.TextField()
        supplier = models.CharField(max_length=255)
        phone_number = models.CharField(max_length=13)

        class Meta:
            db_table ='gym_item'


class gym_trainor(models.Model):
    trainor_id = models.CharField(max_length=255,unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)

    class Meta:
        db_table = 'gym_trainor'


class gym_classes(models.Model):
     class_name = models.CharField(max_length=255)
     class_type = models.CharField(max_length=255)
     class_day = models.CharField(max_length=255)
     class_hour = models.CharField(max_length=255)


     
     # dont forget to connect this gym trainor_name into gym_trainor model
     trainor_name = models.CharField(max_length=255)
    
     class Meta:
        db_table = 'gym_classes'


class member_login(models.Model):
    id_card = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name =models.CharField(max_length=255)
    login =models.CharField(max_length=255)

    class Meta:
        db_table = 'login_record'