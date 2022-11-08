from django.urls import path

#use dot(.) because this function and urls under same the app folder
from .views import user_registration, user_login, user_logout

#use app_name for identifying easily apps urls
app_name = 'User_Auth'

urlpatterns = [
    path('register/', user_registration, name='user_register'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    
]
