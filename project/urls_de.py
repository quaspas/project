from django.conf.urls import include, url
from django.contrib import admin
from project.app.views import HomeView, BlogView, AboutView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^Nachrichten/$', BlogView.as_view(), name='blog'),
    url(r'^etwa/$', AboutView.as_view(), name='about'),
    url(r'^', include('project.app.urls_de')),

    url(r'^i18n/', include('django.conf.urls.i18n')),

    url(r'^admin/', include(admin.site.urls)),
]
