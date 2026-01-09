
from django.contrib import admin
from django.urls import path
from ecom.views import home_page, insert_page


#IMAGE WORK
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('insert-data/', insert_page)

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
