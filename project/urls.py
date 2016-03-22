from django.conf.urls import include, url
from django.contrib import admin
from project.app.views import HomeView, BlogView, AboutView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^blog/$', BlogView.as_view(), name='blog'),
    url(r'^about/$', AboutView.as_view(), name='about'),

    url(r'^i18n/', include('django.conf.urls.i18n')),

    url(r'^admin/', include(admin.site.urls)),
]
