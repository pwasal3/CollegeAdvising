from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('allschools', views.all_schools, name = 'all_schools'),
    path('updateSchoolName', views.updateSchoolName1, name = 'updateSchoolName'),
    path('restoreSchoolName', views.updateSchoolName2, name = 'restoreSchoolName')
]
