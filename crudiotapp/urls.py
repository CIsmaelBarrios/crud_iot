from rest_framework import routers
from .api import CrudIotViewSet
router= routers.DefaultRouter()

router.register('api/crudiotapp', CrudIotViewSet, 'crud')
urlpatterns=router.urls