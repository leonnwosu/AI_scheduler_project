from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import schedule
from .models import scheduleserializer


# Create your views here.
@api_view(['POST'])
def create_schedule(request):
    schedata = scheduleserializer(data = request.data) 

    if schedata.is_valid():
        schedata.save()
        return Response({'message': 'schedule created successfully', 'schedule' : schedata.data}, status=status.HTTP_201_CREATED)
    
    return Response(schedata.errors ,status= status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_all_schedules(request):
    schedata = schedule.objects.all()
    serealized = scheduleserializer(schedata,many = True)
    if serealized.is_valid():
        return Response({'schedule' : serealized.data}, status= status.HTTP_200_OK)
    else:
        return Response(serealized.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_schedule(request, pk):
    Schedule = schedule.objects.get(schedule_id = pk)
    serialize = scheduleserializer(Schedule)
    if serialize.is_valid():
        return Response({'schedule' : serialize.data}, status= status.HTTP_200_OK)
    else:
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_schedule(request,pk):
    try:
        Schedule = schedule.objects.get(schedule_id=pk)
        Schedule.delete()
        return Response({'message': 'schedule successfully deleted'}, status=status.HTTP_200_OK)
    except Schedule.DoesNotExist:
        return Response({'errer':'schedule does not exist'}, status=status.HTTP_404_NOT_FOUND)
        

    