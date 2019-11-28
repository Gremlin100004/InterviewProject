
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('PostApp.urls')),
    path('auth/', include('LogsysApp.urls')),
    path('user/', include('PostApp.urls')),
]
