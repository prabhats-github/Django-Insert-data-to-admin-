from django.db import models

# Create your models here.
class Res(models.Model):
    name=models.CharField(max_length=200)
    mob=models.IntegerField()
    email=models.EmailField()
    # chkin=models.DateField()
    # chkout=models.DateField()
    # adults=models.IntegerField()
    # children=models.IntegerField()
    # room_type=models.CharField(max_length=100)
    # no_of_rooms=models.IntegerField()