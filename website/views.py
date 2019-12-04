from django.shortcuts import render
from django.http import HttpResponse

from website.service import getSchools, getUsers, updateSchoolName, restoreSchoolName

def index(request):
    return HttpResponse(render(request, 'index.html'))
# Create your views here.

def updateSchoolName1(request):
    res = updateSchoolName()
    return HttpResponse(res)

def updateSchoolName2(request):
    res = restoreSchoolName()
    return HttpResponse(res) 

def profile(request):
    return HttpResponse(render(request, 'profile.html'))

def schoolApplied(request):
    return HttpResponse(render(request, 'SchoolsApplied.html'))

def register(request):
    return HttpResponse(render(request, 'register.html'))

def login(request):
    return HttpResponse(render(request, 'login.html'))

def forgotPassword(request):
    return HttpResponse(render(request, 'forgot-password.html'))

def searchSchools(request, searchType, inorout, state, tuition, size, degree, gender):
    schools = getSchools(searchType, inorout, state, tuition, size, degree, gender)

    return HttpResponse(render(request, 'search.html', {'schools': schools}))