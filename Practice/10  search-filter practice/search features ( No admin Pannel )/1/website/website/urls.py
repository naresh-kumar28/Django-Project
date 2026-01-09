from django.contrib import admin
from django.urls import path
from myshop.views import *
from myshop.admin_views import *



#IMAGE WORK
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('superadmin/', admin.site.urls),
    path('', home),
    path('add-category/', addCategory),
    path("insert-data/", insertpage),
    path('product/<int:product_id>/',viewDetails, name="viewDetails"),

    #admin Pannel work

    path('admin/', dashboard, name="admin-dashboard"),
    path('admin/manage-product/', manageProduct, name="manage-product"),
    path('admin/manage-category/', manageCategory, name="manage-category"),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
