"""AlCuMn URL Configuration

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
from ClassHome import views
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

urlpatterns = [
    path('chat.html', views.chat),
    path('index.html', views.index),
    path('lesson.html', views.lesson),
    path('personal.html', views.personal),
    path('portfolio.html', views.portfolio),
    path('subject.html', views.subject),
    path('timetable.html', views.timetable),
    path('admin.html', admin.site.urls)

]
