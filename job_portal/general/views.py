from django.shortcuts import render, redirect
from general.models import recruiter, seeker


# Create your views here.

def index(request):
    return render(request, 'general/index.html')


def login(request):
    return render(request, 'general/login.html')


def Seeker(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        location = request.POST.get('location')
        email = request.POST.get('email')
        experience = request.POST.get('experience')
        password = request.POST.get('password')
        skill = request.POST.get('skill')
        industry = request.POST.get('industry')
        Seeker = seeker(name=name, location=location,
                        email=email, experience=experience, password=password, key_skill=skill,
                        industry=industry)
        Seeker.save()
        response = redirect('/home-seeker/')
        return response

    return render(request, 'general/seeker.html')


def Recruiter(request):
    if request.method == 'POST':
        company_name = request.POST.get('company_name')
        location = request.POST.get('location')
        email = request.POST.get('email')
        name = request.POST.get('name')
        password = request.POST.get('password')
        company_type = request.POST.get('company_type')
        no_emp = request.POST.get('no_emp')
        Recruiter = recruiter(company_name=company_name, location=location,
                              email=email, name=name, password=password, company_type=company_type,
                              no_emp=no_emp)

        Recruiter.save()
        response = redirect('/home-recruiter/')
        return response

    return render(request, 'general/recruiter.html')
