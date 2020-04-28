from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


app_name = 'rest'
urlpatterns = [
    url(r'^$', views.login, name='login'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)