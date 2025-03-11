from django.db import models
from rest_framework import serializers
from users.models import user

# Create your models here.
class schedule(models.Model):
    schedule_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(user, on_delete= models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    calender_name = models.CharField(max_length=255)
    original_url = models.URLField()
    modified_url = models.URLField()

class scheduleserializer(serializers.ModelSerializer):
    class Meta:
        model = schedule
        fields = ['schedule_id', 'user_id', 'date_created', 'calender_name', 'original_url', 'modified_url']