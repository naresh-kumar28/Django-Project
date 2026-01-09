
from django.contrib import admin
from django.urls import path
from myapp.views import home, insert_page

#IMAGE WORK
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('insert-data/', insert_page)

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
