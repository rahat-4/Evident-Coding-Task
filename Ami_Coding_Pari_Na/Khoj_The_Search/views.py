from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from User_Auth.models import MyUser
from .models import ValueList
from .forms import ValueListForm
from .serializers import MyUserSerializer

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

#check current user is logged in or not. If not logged in then pass current user to the login page
@login_required
def home_view(request):
    form = ValueListForm()
    #get current user object model
    user = MyUser.objects.get(email=request.user)
    dict = {}
    found = ""
    if request.method == "POST":
        #get value_list and search value for storing input value and applying query
        value_list = request.POST.get('value_list')
        search_here = request.POST.get('search_here')
        
        #sorting values_list in descending order
        result = ','.join(sorted(value_list.split(","), reverse=True))
        
        form = ValueListForm(request.POST)
        #save user and input values into model
        value = ValueList(user=user, input_values=result)
        value.save()
        
        #check searching value exists or not
        if search_here:
            if search_here in result:
                found = True
            else:
                found = False
                       
    dict.update({"form": form, "found": found})
    return render(request, "Khoj_The_Search/home.html", dict)

# class MyUserView(generics.ListAPIView):
#     queryset = MyUser.objects.all()
#     serializer_class = MyUserSerializer
#     permission_classes = [IsAuthenticated]
    
#     #passing extra data to the serializer class
#     def get_serializer_context(self):
#         context = super().get_serializer_context()
#         context['status'] = 'success'
#         return context
        
    
class MyUserView(APIView):
    def get(self, request, format=None):
        data = MyUser.objects.all()
        serializer = MyUserSerializer(data, many=True, context={'status': 'success'})
            
        return Response(serializer.data)

        
 
        