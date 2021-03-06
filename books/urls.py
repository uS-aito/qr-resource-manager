from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

# django rest framework用
from rest_framework import routers
from .views import BookViewSet, MonitorViewSet

router = routers.DefaultRouter()
router.register(r"books", BookViewSet)
router.register(r"monitors", MonitorViewSet)

urlpatterns = [
    path("", views.index, name="index"),
    path("api/", include(router.urls)),
    path("<str:resource_type>/", views.index, name="index"),
    path("<str:resource_type>/detail/<int:resource_id>", views.detail, name="detail"),
    path("detail/<int:resource_id>", views.detail, name="detail"),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)