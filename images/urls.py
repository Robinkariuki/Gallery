from django.conf.urls import url
from . import views

urlpatterns=[
     url(r'^$',views.images,name='Images'),
     url(r'^search/',views.search_results, name='search_results'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)