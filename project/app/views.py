from django.http.response import Http404
from django.shortcuts import get_object_or_404, render_to_response
from django.views.generic.base import TemplateView
from project.app.models import Page


class HomeView(TemplateView):
    template_name = 'app/index.html'


class BlogView(TemplateView):
    template_name = 'app/blog.html'


class AboutView(TemplateView):
    template_name = 'app/about.html'


class PageView(TemplateView):

    def get(self, request):
        path = request.path_info
        page = get_object_or_404(Page, url=path)
        if request.path_info != page.get_absolute_url():
            raise Http404
        return render_to_response('app/page.html', context={'page': page.name, 'pages':Page.objects.all()})


class PageViewDe(TemplateView):

    def get(self, request):
        path = request.path_info
        page = get_object_or_404(Page, url_de=path)
        if request.path_info != page.get_absolute_url_de():
            raise Http404
        return render_to_response('app/page.html', context={'page': page.name, 'pages':Page.objects.all()})
