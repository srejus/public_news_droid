from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    USER_TYPE_CHOICES = (
        ('public','public'),
        ('reporter','reporter'),
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    pincode = models.CharField(max_length=6,null=True,blank=True)
    gender = models.CharField(max_length=6,null=True,blank=True)
    user_type = models.CharField(max_length=15,default='public',choices=USER_TYPE_CHOICES)

    def __str__(self):
        return str(self.full_name)