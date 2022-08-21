from django.contrib import admin

from .models import *

admin.site.register(Agenda)


def birth(self, obj):
    if obj.birthday:
        return obj.birthday.strftime("%d/%m/%Y")
    birth.empty_value_display = '___/___/_____'