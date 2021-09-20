from app4 import views
from django.urls import path

urlpatterns=[
path('flower/', views.flower, name='flower'),
path('honey/', views.honey, name='honey'),
path('submit/', views.submit, name='submit'),
path('finish/', views.finish, name='finish')

]
