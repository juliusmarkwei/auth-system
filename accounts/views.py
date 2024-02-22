from rest_framework.response import Response
from rest_framework import status
from . import serializers
from django.contrib.auth.models import Group
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi, generators


User = get_user_model()

class GroupView(APIView):
    def get_queryset(self):
        groups = Group.objects.all()
        many = groups.count() > 1
        serializer = serializers.GroupSerializer(groups, many=many)
        return  serializer.data
    
    query_parameter = openapi.Parameter('name', openapi.IN_QUERY, description='Group name', type=openapi.TYPE_STRING)
    response = openapi.Response('List all groups and their permissions', serializers.GroupSerializer)
    @swagger_auto_schema(operation_id='List all groups and their permissions || Specify a group name', manual_parameters=[query_parameter], responses={200: response})
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
    
    response = openapi.Response('Create a group by specifying a name', serializers.GroupSerializer)
    @swagger_auto_schema(operation_id='Create a new group', request_body=serializers.GroupCreateSerializer(), responses={201: response})
    def post(self, request):
        group_name = request.data.get('name')
        if group_name:
            try:
                group = Group.objects.create(name=group_name)
            except Exception as e:
                return Response({'error': f'Group name {group_name} already exists'}, status=status.HTTP_400_BAD_REQUEST)
            group.save()
            return Response({'message': 'Group created successfully'}, status=status.HTTP_201_CREATED)
        return Response({'error': 'You need to specify group name in the request body'}, status=status.HTTP_400_BAD_REQUEST)
    
    
    @swagger_auto_schema(operation_id='Delete a group by specifying a name', request_body=serializers.GroupCreateSerializer(), responses={204: 'Group deleted successfully'})
    def delete(self, request):
        group_name = request.data.get('name')
        if group_name:
            try:
                group = Group.objects.get(name=group_name)
            except Group.DoesNotExist:
                return Response({'error': f'Group name {group_name} does not exist'}, status=status.HTTP_404_NOT_FOUND)
            group.delete()
            return Response({'message': 'Group deleted successfully'}, status=status.HTTP_200_OK)
        return Response({'error': 'You need to specify group name in the request body'}, status=status.HTTP_400_BAD_REQUEST)
    
    

class ManageGroup(APIView):
    @swagger_auto_schema(operation_id='Add a user to a group', request_body=serializers.AddUserToGroupSerializer(), responses={201: 'User added to group successfully'})
    def post(self, request):
        data = request.data
        if data:
            try:
                user_tobe_added = data['username']
                group_name = data['group']
            except KeyError:
                return Response({'error': 'You need to specify both username and group name'}, status=status.HTTP_400_BAD_REQUEST)
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
        return Response({'error': 'You need to specify both username and group name'}, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(operation_id='Remove a user from a group', request_body=serializers.AddUserToGroupSerializer(), responses={200: 'User removed from group successfully'})
    def delete(self, request):
        data = request.data
        if data:
            try:
                user_tobe_added = data['user']
                group_name = data['group']
            except KeyError:
                return Response({'error': 'You need to specify both username and group name'}, status=status.HTTP_400_BAD_REQUEST)
            try:
                user_instance = User.objects.get(username=user_tobe_added)
            except User.DoesNotExist:
                return Response({'error': f'User {user_tobe_added} does not exist!'}, status=status.HTTP_400_BAD_REQUEST)
            try:
                group = Group.objects.get(name=group_name)
            except Group.DoesNotExist:
                return Response({'error': f'Group {group_name} does not exist!'}, status=status.HTTP_400_BAD_REQUEST)
            user_instance.groups.remove(group)
            return Response(status=status.HTTP_200_OK)
        return Response({'error': 'You need to specify both username and group name'}, status=status.HTTP_400_BAD_REQUEST)
    