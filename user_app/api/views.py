from user_app.api.serializers import UserRegistration
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from user_app import models
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserRegistration(data=request.data)
        
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            
            token = Token.objects.get(user=account)
            
            data['username'] = account.username
            data['email'] = account.email
            data['token'] = token.key
            
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = serializer.errors
            return Response(data, status=status.HTTP_400_BAD_REQUEST)