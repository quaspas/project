from django.db import models


class Page(models.Model):

    name = models.CharField(max_length=100)

    url = models.CharField(max_length=100)
    url_de = models.CharField(max_length=100)

    def get_absolute_url(self):
        return self.url

    def get_absolute_url_de(self):
        return self.url_de
