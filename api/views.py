from django.shortcuts import render
from django.http import JsonResponse 
from rest_framework.decorators  import api_view 
from .serializers import RegisterSerializer
from rest_framework.response import Response
from django.http import HttpResponse
from account.models import User


@api_view(['POST'])
def register(request):
    
    first_name = request.data['first_name']
    last_name = request.data['last_name']
    email  = request.data['email']
    phone_number = request.data['phone_number']
    photo = request.data['photo']
    country = request.data['country']


    User.objects.create(first_name=first_name,
                                last_name=last_name,
                                email=email,
                                phone_number=phone_number,
                                photo=photo,
                                username=email,
                                country=country)
    
    
    return HttpResponse({'success message': 'User created'}, status=200)
    

    


@api_view(['POST'])
def login(request):
    pass