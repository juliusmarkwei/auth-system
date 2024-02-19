from djoser import serializers
from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.http import HttpResponse
from . import serializers
from . import forms


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def home(request):
    if request.method == 'GET':
        return render(request, 'accounts/home.html', {})
    

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def signin(request):
    if request.method == 'POST':
        form = request.POST
        
        return HttpResponse('Signin page')
    
    form = forms.UserCreateForm()
    return render(request, 'accounts/signin.html', {'form': form})


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def signup(request):
    if request.method == 'POST':
        form = forms.UserCreateForm(request.POST)
        if form.is_valid():
            serializer = serializers.UserCreateSerializer(data=form.cleaned_data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return render(request, 'accounts/activate.html', {})
        raise ValueError('Invalid form data')
    
    form = forms.UserCreateForm()
    return render(request, 'accounts/signup.html', {'form': form})

