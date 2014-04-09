from django.contrib import admin
from .models import Foo, Bar


class BarInlines(admin.StackedInline):
    model = Bar


class FooAdmin(admin.ModelAdmin):
    inlines = [BarInlines, ]


admin.site.register(Foo, FooAdmin)
admin.site.register(Bar)