from django.urls import path, include
from rest_framework import routers

from users.views import UserView

router = routers.DefaultRouter()
router.register(r'users', UserView, basename='user')

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('registration/', include('dj_rest_auth.registration.urls'))
]

urlpatterns += router.urls
