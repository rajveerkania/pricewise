from django.urls import path
from . import views
urlpatterns = [
    path('', views.homeView, name = 'index'),
    path('result.html', views.resultView, name = 'result'),
    path('about.html', views.aboutView, name = 'about'),
    # path('404.html', views.noResultView, name = '404'),
]