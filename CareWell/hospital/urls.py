from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('booking/',views.booking,name='booking'),
    path('contacts/',views.contacts,name='contacts'),
    path('department/',views.department,name='department'),
    path('doctors/',views.doctors,name='doctors'),
    
]