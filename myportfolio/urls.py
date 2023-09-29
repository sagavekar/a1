from django.contrib import admin
from django.urls import path
from myportfolio import view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin', admin.site.urls),
    path('', view.Home , name="Home"),
    path('contact', view.contact , name="contact"),

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
