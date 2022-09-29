from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('card', CreateCard),
router.register('music', CreateMusic),
router.register('user', User),