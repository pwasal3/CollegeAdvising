from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('updateSchoolName', views.updateSchoolName1, name = 'updateSchoolName'),
    path('restoreSchoolName', views.updateSchoolName2, name = 'restoreSchoolName'),
    path('profile', views.profile, name = 'profile'),
    path('schoolsApplied', views.schoolApplied, name = 'schoolsApplied'),
    path('login', views.login, name = 'login'),
    path('register', views.register, name = 'register'),
    path('logout', views.logout, name = 'logout'),
    path('search=<int:searchType>&inoutstate=<int:inorout>&state=<str:state>&tuition=<int:tuition>&enrollment=<int:size>&degree=<int:degree>&gender=<int:gender>', views.searchSchools, name = 'seachSchools'),
    path('applied', views.findApplied, name = 'applied')
] 
