from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('e_commerce_website.common.urls')),
    path('', include('e_commerce_website.jewelry.urls')),
]
