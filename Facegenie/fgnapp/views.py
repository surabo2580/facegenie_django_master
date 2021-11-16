from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.conf import settings
from Facegenie.settings import BASE_DIR
from fgnapp.models import TriggerApp
import os
import json
import yaml




# Create your views here.
def home(request):
    return render(request, 'home.html')


def displaying_info_model(request):
    triggring_data = TriggerApp.objects.all()
    print("showing details " + str(triggring_data))
    
    #with open("D:\facegenie_project_django\Facegenie\json_data\data.json", "w+") as f:
        #json.dumps(triggring_data, f)
    #json.dumps(triggring_data)
    #return triggring_data

    return render(request,'model.html',{'triggring_data':triggring_data[0]})


def saving_json(request):
    #print ("triggered")
    #showport = TriggerApp.objects.filter(triggring_data = triggring_data).first()
    #print ("showing port" + str(showport))
    #triggring_data = TriggerApp.objects.filter(showport = showport)
    triggring_data = TriggerApp.objects.all()


    #with open(os.path.join(BASE_DIR,'k8s','test.json'), "w") as f:
        #f.writelines(str(triggring_data))

    with open(os.path.join(BASE_DIR,'k8s','data.yml'), "w") as f:
        yaml.dump(triggring_data, f)
    
    return render(request,'save.html')



def Trigger(request):
    
    current_user = request.user
    if current_user is not None : 
       allstatus = TriggerApp.objects.all()
       context = {'allstatus':allstatus}

    if request.method =="POST":
        # Get the post parameters

        portValue = request.POST['portV']
        path = request.POST['path']
        appname = request.POST['appname']

        Trigger = TriggerApp(port=portValue,path=path,appname=appname)
        Trigger.save()
        #return render(request,'model.html')
        return render(request,'modelTrigger.html',context)


    else:

        return render(request,'register.html')


def handleSignup(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['username']
        email = request.POST['email']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # check for errorneous input
        if len(username) > 10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('fgn')
        if username.isalpha():
            messages.error(request, "username can't only contains alphabet")
            return redirect('fgn')
        if username.isnumeric():
            messages.error(request, "username can't only contain numeric value")
            return redirect('fgn')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('fgn')
        if User.objects.filter(username=username).exists():
            messages.error(request, "username already exists")
            return redirect('fgn')
        if User.objects.filter(email=email).exists():
            messages.error(request, "email already exists")
            return redirect('fgn')
        if pass1 != pass2:
            messages.error(request, " Passwords do not match")
            return redirect('fgn')

        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.save()
        messages.success(request, " Your accounts has been successfully created")
        return redirect('fgn')

    else:
        return HttpResponse("404 - Not found")


def handlelogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #captcha = request.POST.get('cap')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'successfully logged in')
            return redirect('Trigger')
        else:
            messages.error(request, 'invalid credentials')
            return redirect('fgn')
    #messages.error(request, 'invalidcaptcha')
    return redirect('fgn')


def handlelogout(request):
    logout(request)
    messages.success(request,'you have successfully logged out')
    return redirect('fgn')