from . import views
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('home', views.home, name='home'),
    path('signin', views.signin, name='signin'),
    path('auth/users/', views.signup),
]
