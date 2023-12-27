from django.urls import path, include, re_path
from .views import MedicineAPIViewSet, CategoriesAPIViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"products", MedicineAPIViewSet)
router.register(r"categories", CategoriesAPIViewSet)

urlpatterns = [
    path('', include(router.urls))
]
