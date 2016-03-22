from django.conf.urls import url, patterns

from project.app.models import Page
from project.app.views import PageView


def make_page_url(page, **kwargs):
    return url('^{}$'.format(page.get_absolute_url().lstrip('/')), PageView.as_view(), **kwargs)


urlpatterns = patterns('', url(r'^/$', PageView.as_view(), name='pages'), )

for page in Page.objects.exclude(url=''):
    kwargs = {'name': page.name}
    urlpatterns += patterns('', make_page_url(page, **kwargs))
