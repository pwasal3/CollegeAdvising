from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('allschools', views.all_schools, name = 'all_schools'),
    path('updateSchoolName', views.updateSchoolName1, name = 'updateSchoolName'),
    path('restoreSchoolName', views.updateSchoolName2, name = 'restoreSchoolName'),
    path('myProfile', views.profile, name = 'profile'),
    path('schoolsApplied', views.schoolApplied, name = 'schoolsApplied'),
    path('login', views.login, name = 'login'),
    path('register', views.register, name = 'register'),
    path('forgotPassword', views.forgotPassword, name = 'forgotPassword')
] 
