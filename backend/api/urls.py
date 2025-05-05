# backend/api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet

router = DefaultRouter(trailing_slash=False)   # ← no “/” at the end
# equivalent:  SimpleRouter(trailing_slash=False)

router.register(r'', ItemViewSet, basename='items')

urlpatterns = router.urls          # no need for an extra list wrapper
