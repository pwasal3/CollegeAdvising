from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name = 'index'),
    path('allschools', views.all_schools, name = 'all_schools'),
    path('updateSchoolName', views.updateSchoolName1, name = 'updateSchoolName'),
    path('restoreSchoolName', views.updateSchoolName2, name = 'restoreSchoolName')
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
