from .views import GroupView, ManageGroup
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('group', GroupView.as_view(), name='group-view'),
    path('manage-group', ManageGroup.as_view(), name='manage-group'),
]
