from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

from website.service import getSchools, getUsers, updateSchoolName, restoreSchoolName, registerUser, loginUser, getUser, getAppliedSchools
from website.fireservice import readProfileFirebase
from website.predict import filterByPrediction

def index(request):
    if 'user' in request.session:
        user = getUser(request.session['user'])
        return HttpResponse(render(request, 'index.html', {'currentUser': user }))
    else:
        return HttpResponse(render(request, 'login.html'))

# Create your views here.

def updateSchoolName1(request):
    res = updateSchoolName()
    return HttpResponse(res)

def updateSchoolName2(request):
    res = restoreSchoolName()
    return HttpResponse(res) 

def profile(request):
    if 'user' in request.session:
        user = getUser(request.session['user'])
        return HttpResponse(render(request, 'profile.html', {'currentUser': user }))
    else:
        return HttpResponse(render(request, 'login.html'))

def schoolApplied(request):
    if not 'user' in request.session:
        return HttpResponse(render(request, 'login.html'))
        
    userId = request.session['user']
    user = getUser(userId)
    schools = getAppliedSchools(userId)

    print("num schools applied to",len(schools))
    return HttpResponse(render(request, 'SchoolsApplied.html', {'schools': schools, 'currentUser': user }))

def register(request):
    if request.method == 'GET':
        return HttpResponse(render(request, 'register.html'))
    if request.method == 'POST':
        print("registering user")
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        user = registerUser(first_name, last_name, email, password)
        request.session['user'] = user.id
        return redirect('profile')

def login(request):
    if request.method == 'GET':
        return HttpResponse(render(request, 'login.html'))
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = loginUser(email, password)
        
        request.session['user'] = user.id
        return redirect('profile')

def logout(request):
    if 'user' in request.session:
        del request.session['user']
    return redirect('login')


def searchSchools(request, searchType, inorout, state, tuition, size, degree, gender):
    print("searchtype", searchType)
    if not 'user' in request.session:
        return HttpResponse(render(request, 'login.html'))

    userId = request.session['user']
    profile = readProfileFirebase(userId)
    
    print("searching schools")
    schools = getSchools(searchType, inorout, state, tuition, size, degree, gender)
    
    schools = filterByPrediction(searchType, schools, profile)
    return HttpResponse(render(request, 'search.html', {'schools': schools}))