from project.app.models import Page


def constants(request):
    return {
        'pages': Page.objects.all(),
    }
