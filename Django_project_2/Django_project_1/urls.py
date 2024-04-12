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
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    #VIEWS AND CREATE URLS
    path('small_farms_app/Item/', views.item_view, name='infrastructure_item_view'),
    path('small_farms_app/InfrustructureType/', views.type_view, name='infrastructure_type_view'),
    path('small_farms_app/LogAction/', views.log_action_view, name='log_action_view'),
    path('small_farms_app/ManagmentLog/', views.managment_log_view, name='management_log_view'),
    #DELETE URLS
    path('item/<int:item_id>/delete/', views.delete_item, name='delete_item'),
    path('type/<int:type_id>/delete/', views.delete_type, name='delete_type'),
    path('managment_log/<int:log_id>/delete/', views.delete_log, name='delete_log'),
    path('log_action/<int:action_id>/delete/', views.delete_action, name='delete_action'),
    #DETAIL PAGE URLS
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('type/<int:type_id>/', views.type_detail, name='type_detail'),
    path('managment_log/<int:log_id>/', views.managment_log_detail, name='managment_log_detail'),
    path('log_action/<int:action_id>/', views.log_action_detail, name='log_action_detail'),


]