from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, LoginForm
# Create your views here.

#registration function
def user_registration(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(data=request.POST)

        #check form is valid or not
        if form.is_valid():
            form.save()
            #after validation and saving pass user to the login page
            return HttpResponseRedirect(reverse("User_Auth:user_login"))

    #create dictionary for sending registration form to the html page
    dict = {'form':form}
    return render(request, "User_Auth/user_register.html", dict)

#user login function
def user_login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(data=request.POST)
        
        #get username and password for checking authentication
        username = request.POST.get("username")
        password = request.POST.get("password")

        if form.is_valid():
            auth = authenticate(username=username, password=password)
            
            #if user is authenticated then pass user to the home page
            if auth:
                login(request, auth)
                return HttpResponseRedirect(reverse("Khoj_The_Search:home")) 
            else:
                return HttpResponse("Access deined!")

    #create dictionary for sending login form to the html page
    dict = {'form':form}
    return render(request, "User_Auth/user_login.html", dict)

#check current user is logged in or not. If not logged in then pass current user to the login page
@login_required
def user_logout(request):
    logout(request)
    
    #send back current user to the login page after logout
    return HttpResponseRedirect(reverse("User_Auth:user_login"))