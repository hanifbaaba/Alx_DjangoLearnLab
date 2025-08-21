from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.

class UserView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [ IsAuthenticated]


    def get(self,request):
        return request({"message": f"Hello{request.user.username}, you are authenticated!"})