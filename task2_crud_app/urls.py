from django.urls import path
from . import views

app_name = 'crud_app'

urlpatterns = [
    path('', views.display_all_users, name='display_all_users'),
    path('api/', views.create_user, name='create_user'),
    path('api/<int:user_id>', views.display_user, name='display_user'),
]

