from django.urls import path
from rest_framework.routers import SimpleRouter


from .api import CustomUserViewSet


app_name = 'accounts'


router = SimpleRouter()
router.register('api/users', CustomUserViewSet)


urlpatterns = [
    
]


urlpatterns += router.urls
