from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:resource_id>/", views.info, name="info"),
    path("<int:resource_id>/reserve/", views.reserve, name="reserve"),
    path("<int:resource_id>/release/", views.release, name="vote"),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)