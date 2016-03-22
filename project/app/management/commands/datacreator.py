from django.contrib.auth.models import User

from django.core.management.base import BaseCommand

from project.app.models import Page


class Command(BaseCommand):
    def create_users(self):
        def create_user_helper(email, is_staff=False):
            user = User.objects.get_or_create(email=email)[0]
            user.is_staff = is_staff
            user.set_password('password')
            user.is_active = True
            user.save()
            return user
        create_user_helper('superuser@example.com', is_staff=True)

    def create_pages(self):
        def make_page(url, url_de, name):
            Page.objects.create(url=url, url_de=url_de, name=name)

        make_page('/contest', '/wettbewerb', 'contest')
        make_page('/contest/winner', '/wettbewerb/gewinner', 'win')
        make_page('/contest/looser', '/wettbewerb/verlierer', 'lose')


    def handle(self, *args, **options):
        self.create_users()
        self.create_pages()
