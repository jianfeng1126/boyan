from django.contrib import admin
from django.urls import path
from dept import views
urlpatterns = [

    path('listdazhong/', views.listdazhong),
    path('delete/', views.delete),
    path('toadd/', views.toadd),
    path('add/', views.add),
    path('info/', views.info),
    path('update/', views.update),
    path('listlike/', views.listlike),
]