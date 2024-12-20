from django.contrib import admin
from django.urls import path

admin.site.site_header = "chintan site header changes"
admin.site.site_title = "chintan site title"

urlpatterns = [
    path('admin/', admin.site.urls),
]
