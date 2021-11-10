from django.contrib import admin
from main import views
from django.core.wsgi import get_wsgi_application
from django.urls import include, path

application = get_wsgi_application()

urlpatterns = [
    path('', views.chat, name='chat'),
    path('<str:room_name>/', views.room, name='room'),
    path('index.html', views.index),
    path('lesson.html', views.lesson),
    path('personal.html', views.personal),
    path('portfolio.html', views.portfolio),
    path('subject.html', views.subject),
    path('timetable.html', views.timetable),
    path('admin/', admin.site.urls),
]
