from app4 import views
from django.urls import path

urlpatterns=[
   path('flower/', views.flower, name='floe'),
   path('honey/', views.honey, name='bee'),
   path('submit/', views.submit, name='submit'),
   path('finish/', views.finish, name='fin')

]
