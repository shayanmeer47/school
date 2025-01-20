from django.shortcuts import render, redirect
import django.http as http
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.

def index(request):
    school = "AL- mashriq public school Skardu"
    schoolBranch = "AL- mashriq public school Khaplu"

    data = {
        'schoolName': school,
        'schoolBranchName': schoolBranch
    }
    return render(request, 'school/AMPS.html', {'data': data})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(email=username).exists():
            user = User.objects.get(email=username)
            if user.check_password(password):
                authenticatedUser = authenticate(email=username, password=password)
                data = {
                    'user': authenticatedUser
                }
                return redirect('index')
            else:
                data = {
                    'error': "Invalid password"
                }
                return render(request, 'school/login.html', {'data': data})
        else:
            data = {
                'error': "Invalid email or password"
            }
            return render(request, 'school/login.html', {'data': data})
        
    return render(request, 'school/login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first']
        last_name = request.POST['last']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']
        if password == repassword:
            if User.objects.filter(email=email).exists():
                data = {
                    'error': "User already exists"
                }
                return render(request, 'school/reg.html', {'data': data})
            
            user = User.objects.create_user(first_name + last_name, email, email)
            user.set_password(password)
            user.save()
            data = {
                'message': "User created successfully"
            }
            return redirect('login')
        else:
            data = {
                'error': "Passwords do not match"
            }
            return render(request, 'school/reg.html', {'data': data})
    return render(request, 'school/reg.html')