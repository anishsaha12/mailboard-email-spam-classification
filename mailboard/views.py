from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from employee.models import Employee

# Create your views here.
def app_login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        try:
            logged_in_user = authenticate(username=username, password=password)
        except:
            context = dict()
            context['error'] = 'The user could not be logged in'
            print("ERROR",context)
            return render(request, 'mailboard/signin.html', context)
        
        if logged_in_user is None:
            context = dict()
            context['error'] = 'The user could not be logged in'
            print("ERROR",context)
            return render(request, 'mailboard/signin.html', context)

        if Employee.objects.filter(user=logged_in_user).exists():
            login(request, logged_in_user)
            return HttpResponseRedirect('home/')
        else:
            context = dict()
            context['error'] = 'This user is not registered for this platform'
            print("ERROR",context)
            return render(request, 'mailboard/signin.html', context)

    return render(request, 'mailboard/signin.html', {})

def app_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def app_home(request):
    return render(request, 'mailboard/home.html', {})