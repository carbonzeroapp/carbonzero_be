from django.contrib import admin
from django.urls import path, include

proxy_service_name = 'data-management'

urlpatterns = [
    path(f'api/{proxy_service_name}/admin/', admin.site.urls),
]
