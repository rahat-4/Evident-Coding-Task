from django.urls import path

#use dot(.) because this function and urls under same the app folder
from .views import home_view, MyUserView

#use app_name for identifying easily apps urls
app_name = 'Khoj_The_Search'

urlpatterns = [
        path('', home_view, name='home'),
        path('api/list/', MyUserView.as_view(), name='input_data'),
]