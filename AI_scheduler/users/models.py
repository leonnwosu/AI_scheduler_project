from django.db import models
from rest_framework import serializers

# Create your models here.
class user (models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255, unique= True)
    password_hash = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def str(self):
        return self.user_name


# serelaizer to tranform to json
class userserelaizer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['user_id', 'user_name', 'password_hash', 'email']