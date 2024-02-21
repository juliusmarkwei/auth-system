from rest_framework.response import Response
from rest_framework import status
from . import serializers
from django.contrib.auth.models import Group
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import get_user_model

User = get_user_model()

class GroupView(APIView):
    def get_queryset(self):
        groups = Group.objects.all()
        many = groups.count() > 1
        serializer = serializers.GroupSerializer(groups, many=many)
        return  serializer.data
    
    def get(self, request):
        if request.query_params:
            group_name = request.query_params.get('name')
            try:
                group = Group.objects.get(name=group_name)
                serializer = serializers.GroupSerializer(group)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Group.DoesNotExist:
                return Response({'error': f'Group name {group_name} does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        groups = self.get_queryset()
        return Response(groups, status=status.HTTP_200_OK)
    
    def post(self, request):
        if request.POST['name']:
            group_name = request.POST['name']
            group = Group.objects.create(name=group_name)
            group.save()
            return Response({'message': 'Group created successfully'}, status=status.HTTP_201_CREATED)
        return Response({'error': 'You need to specify group name in the request body'}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        if request.POST['name']:
            group_name = request.POST['name']
            group = Group.objects.get(name=group_name)
            group.delete()
            return Response({'message': 'Group deleted successfully'}, status=status.HTTP_200_OK)
        return Response({'error': 'You need to specify group name in the request body'}, status=status.HTTP_400_BAD_REQUEST)
    
    

class ManageGroup(APIView):
    def post(self, request):
        data = request.data
        user_tobe_added = data['user']
        group_name = data['group_name']
        
        try:
            user_instance = User.objects.get(username=user_tobe_added)
        except User.DoesNotExist:
            return Response({'error': f'User {user_tobe_added} does not exist!'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            group = Group.objects.get(name=group_name)
        except Group.DoesNotExist:
            return Response({'error': f'Group {group_name} does not exist!'}, status=status.HTTP_400_BAD_REQUEST)
        user_instance.groups.add(group)
        return Response(status=status.HTTP_201_CREATED)
    
    