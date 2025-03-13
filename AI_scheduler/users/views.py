from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import user
from .models import userserelaizer

# Create your views here.
@api_view(['POST'])
def create_user(request):
    serializer = userserelaizer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()  # Saves data to the database
        return Response({'message': 'User created successfully', 'user': serializer.data}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_user(request, cemail, cpassword):
    try:
        User = user.objects.get(email = cemail, password_hash = cpassword )
        serialize = userserelaizer(User)
        return Response(serialize.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error' : str(e)}, status=status.HTTP_400_BAD_REQUEST)