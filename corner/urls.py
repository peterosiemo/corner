
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('coreapp.urls')),
    path('', include('accountsapp.urls')),
    path('', include('menuapp.urls')),
    path('', include('reservationsapp.urls')),
    path('', include('orders.urls')),
    path('', include('payments.urls')),
    path('', include('admin1app.urls')),
    path('', include('staff.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
