from django.db import models
from users.models import user
from rest_framework import serializers

# Create your models here.


class event(models.Model):

    event_type_fields = [
        ('Original','original'),
        ('User-added', 'user-added'),
        ('AI-added', 'ai-added')
    ]
    event_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(user,on_delete=models.CASCADE)
    event_type = models.CharField(max_length=255 ,choices= event_type_fields,default= 'User added')
    event_title = models.CharField(max_length=255)
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
    event_description = models.CharField(max_length=2083)


class eventSerializer(serializers.Serializer):
    class Meta:
        model = event
        fields = ['event_id','schedule_id','event_type','event_title','start_date_time','end_date_time','event_description']
