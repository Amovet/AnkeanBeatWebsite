
from rest_framework import routers
from .api import PlaylistViewSet


router = routers.DefaultRouter()
router.register('api/playlist', PlaylistViewSet, 'PlayList')


urlpatterns = router.urls
