"""
URL configuration for myproject1 project.

#약속: urlpatterns 반드시 정의하기 (라우팅과 관련된 정보)
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
# http://127.0.0.1/ #(home)
# http://127.0.0.1/app/

# http://127.0.0.1/create/
# http://127.0.0.1/read/1/
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls'))
]
