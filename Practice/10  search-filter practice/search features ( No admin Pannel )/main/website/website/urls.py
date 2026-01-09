from django.contrib import admin
from django.urls import path
from myshop.views import *



#IMAGE WORK
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('add-category/', addCategory),
    path("insert-data/", insertpage),
    path('product/<int:product_id>/',viewDetails, name="viewDetails")

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
