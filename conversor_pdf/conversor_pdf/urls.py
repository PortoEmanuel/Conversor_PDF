from django.contrib import admin
from django.urls import path, include
from site_conversor_pdf import views

urlpatterns = [
    path('', include('site_conversor_pdf.urls')),
    path('admin/', admin.site.urls),
]
