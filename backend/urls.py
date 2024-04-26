"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static


from .swagger import schema_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path('employees/', include('employees.urls', namespace="employees")),
    path('educational_degrees/', include('educational_degrees.urls', namespace="educational_degrees")),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Панель адміністрування для сайту кафедри Інтелектуальних систем'
admin.site.index_title = 'Сайт кафедри'
