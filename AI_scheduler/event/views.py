from django.shortcuts import render
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

@api_view(['POST'])
def add_event(request):
    try:
        newEvent = event(data = request.data)
        serialized = eventSerializer(newEvent)
        serialized.save()
        return Response({'message' : 'event added to calender'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error' : str(e)}, status= status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def get_events(request, pk):
    try:
        events = event.objects.filter(user_id = pk).order_by(event.start_date_time)
        if not events.exists():
            return Response({'message' : 'no events for this user'}, status=status.HTTP_204_NO_CONTENT)
        
        serelized = eventSerializer(events,many = True)
        return Response(serelized.data, status=status.HTTP_200_OK)
    except event.DoesNotExist:
        return Response({'error' : 'user not found'}, status = status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error' : str(e)}, status=status.HTTP_404_NOT_FOUND)
    

@api_view(['GET'])
def get_one_event(request, pk, uk):
    try:
        theEvent = event.objects.get(user_id = uk, event_id = pk)
        if not theEvent.exists():
            return Response({'message' : 'Event not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serialize = eventSerializer(theEvent)
        return Response(serialize.data,status=status.HTTP_200_OK)
   
    except Exception as e:
        return Response({'error' : str(e)}, status= status.HTTP_400_BAD_REQUEST)