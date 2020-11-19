from django.conf.urls import url

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^projects/$', views.projects, name='projects'),
    url(r'^resume/$', views.resume, name='resume'),
    url(r'^memory_game/$', views.memory_game, name='memory_game'),
    url(r'^download/(?P<filename>.*)$', views.download_zip, name='download_zip'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)