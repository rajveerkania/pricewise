from django.urls import path
from . import views
urlpatterns = [
    path('', views.homeView, name = 'index'),
    path('result.html', views.resultView, name = 'result')
]

