from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = 'app/index.html'


class BlogView(TemplateView):
    template_name = 'app/blog.html'


class AboutView(TemplateView):
    template_name = 'app/about.html'
