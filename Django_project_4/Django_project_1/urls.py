"""Django_project_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from small_farms_app import views


urlpatterns = [
    #SMALL_FARMS

    path('admin/', admin.site.urls),
    path('index/', views.IndexView.as_view(), name='index'),
    #VIEWS AND CREATE URLS
    path('small_farms_app/Item/', views.ItemView.as_view(), name='infrastructure_item_view'),
    path('small_farms_app/InfrustructureType/', views.TypeView.as_view(), name='infrastructure_type_view'),
    path('small_farms_app/LogAction/', views.LogActionView.as_view(), name='log_action_view'),
    path('small_farms_app/ManagmentLog/', views.ManagementLogView.as_view(), name='management_log_view'),
    #DELETE URLS
    path('item/<int:item_id>/delete/', views.DeleteItemView.as_view(), name='delete_item'),
    path('type/<int:type_id>/delete/', views.DeleteTypeView.as_view(), name='delete_type'),
    path('log/<int:log_id>/delete/', views.DeleteLogView.as_view(), name='delete_log'),
    path('action/<int:action_id>/delete/', views.DeleteActionView.as_view(), name='delete_action'),

    #DETAIL PAGE URLS
    path('item/<int:item_id>/', views.ItemDetailView.as_view(), name='item_detail'),
    path('type/<int:type_id>/', views.TypeDetailView.as_view(), name='type_detail'),
    path('managment_log/<int:log_id>/', views.ManagementLogDetailView.as_view(), name='managment_log_detail'),
    path('log_action/<int:action_id>/', views.LogActionDetailView.as_view(), name='log_action_detail'),



]

from django.contrib import admin
from django.urls import path
from wildlife import views

urlpatterns = [

    path('admin/', admin.site.urls),
]