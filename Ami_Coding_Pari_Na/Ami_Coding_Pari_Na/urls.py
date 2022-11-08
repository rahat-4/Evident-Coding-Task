from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Khoj_The_Search.urls')),
    path('accounts/', include('User_Auth.urls'))
]
