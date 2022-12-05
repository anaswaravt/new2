from django.urls import path
from.import views
urlpatterns = [
    path('index/',views.index,name='index'),
    path('',views.mainhome,name='mainhome'),
    path('contact/',views.contact,name='contact'),
    path('course/',views.Course,name='course'),

]