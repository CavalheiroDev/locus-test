"""fronttest URL Configuration

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
from fronttest.settings import STATIC_ROOT
from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import RedirectView
from django.views.static import serve
import consumeApi.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/1')),
    path('<int:number_page>', consumeApi.views.home),
    re_path(r'static/(?P<path>.*)$', serve,
            {'document_root': STATIC_ROOT})
]
