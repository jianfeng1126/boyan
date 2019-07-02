from django.contrib import admin
from django.urls import path
from user import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('toadd/', views.toadd),
    # path('useradd/', views.useradd),
    path('', views.login),
    path('index/', views.index)

]