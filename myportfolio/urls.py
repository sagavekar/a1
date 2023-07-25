from django.contrib import admin
from django.urls import path
from myportfolio import view
from api import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.Home),
    path('studentapi/',views.StudentAPI.as_view() ),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
