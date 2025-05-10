from rest_framework.routers import DefaultRouter
from .views import AdminLogViewSet

router = DefaultRouter()
router.register(r'admin-logs', AdminLogViewSet, basename='admin-log')

urlpatterns = router.urls
