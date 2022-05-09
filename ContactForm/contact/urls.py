from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_view,name='contact_view'),
    path('success', views.success,name='success')
]