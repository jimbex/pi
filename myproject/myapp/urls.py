from django.urls import path
from . import views

urlpatterns = [
    path('', views.logins, name='login'),
    path('/welcome', views.welcome, name='welcome'),
    path('/main', views.main, name='main'),
    path('/final', views.final, name='final'),
    path('/stream-video', views.stream_video, name='video-feed')
    
]
