from django.contrib import admin
from .models import Type_of_med, Medicine

admin.site.register(Medicine)
admin.site.register(Type_of_med)