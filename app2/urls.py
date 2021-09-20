from app2 import views
from django.urls import path

urlpatterns=[
path('pavi/', views.byeall, name='pavi'),
path('dinesh/', views.pavi, name='dinesh')

]
