from django.shortcuts import render, redirect
from general.models import recruiter, seeker
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'general/index.html')

def about(request):
    return render(request, 'general/about.html')

def team(request):
    return HttpResponse("our team")

def terms(request):
    return HttpResponse("terms of use")

def faq(request):
    return HttpResponse("faqs")

def login_seeker(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        print(user)

        if user is not None:
            auth.login(request, user)
            response = redirect('/home-seeker/')
            return response
            
        else:
            messages.info(request, "ivalid username or password")
            return render(request, 'general/logins.html')
    return render(request, 'general/logins.html')

def login_recruiter(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        print(user)

        if user is not None:
            auth.login(request, user)
            response = redirect('/home-recruiter/')
            return response
            
        else:
            messages.info(request, "ivalid username or password")
            return render(request, 'general/loginr.html')
    return render(request, 'general/loginr.html')



def Seeker(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        location = request.POST.get('location')
        email = request.POST.get('email')
        experience = request.POST.get('experience')
        username = request.POST.get('username')
        password = request.POST.get('password')
        skill = request.POST.get('skill')
        industry = request.POST.get('industry')
        if password == confirmpassword:
            if User.objects.filter(username=username).exists:
                messages.info(request, 'Username Already Taken')
                return render(request, 'general/seeker.html')
            elif User.objects.filter(username=username).exists:
                messages.info(request, 'Email Already Taken')
                return render(request, 'general/seeker.html')
            else:
                new_seeker = User.objects.create_user(username=username,email=email,password=password, first_name=name)
                new_seeker.save()
                Seeker = seeker(name=name, location=location,usernname=username,email=email, experience=experience, password=password, key_skill=skill,
                        preferred_industry=industry)
                Seeker.save()
                response = redirect('/home-seeker/')
                return response
        else:
            messages.info(request, 'Passwords did not match')
            return render(request, 'general/seeker.html')
    print(User.objects.all().values_list('username'))        
    return render(request, 'general/seeker.html')


def Recruiter(request):
    if request.method == 'POST':
        name = request.POST.get('companyname')
        email = request.POST.get('email')
        location = request.POST.get('location')
        industry = request.POST.get('industry')
        no_emp = request.POST.get('emp')
        website = request.POST.get('website')
        linkedin = request.POST.get('linkedin')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        if password == confirmpassword:
            if User.objects.filter(username=username).exists:
                return render(request, 'general/seeker.html')
            elif User.objects.filter(username=username).exists:
                return render(request, 'general/seeker.html')
            else:
                new_recruiter = User.objects.create_user(username=username,email=email,password=password, first_name=name)
                new_recruiter.save()
                Recruiter = recruiter(company_name=name, location=location,
                        email=email, website=website, linkedin=linkedin ,password=password, no_emp=no_emp,
                        Industry=industry)
                Recruiter.save()
                response = redirect('/home-recruiter/')
                return response
        else:
                    messages.info(request, 'Passwords did not match')
                    return render(request, 'general/recruiter.html')
    return render(request, 'general/recruiter.html')

