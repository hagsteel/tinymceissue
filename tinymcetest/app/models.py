from django.db import models
from tinymce.models import HTMLField


class Foo(models.Model):
    val = models.CharField(max_length=100)


class Bar(models.Model):
    entry = HTMLField()
    foo = models.ForeignKey(Foo)
