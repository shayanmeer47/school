from django.contrib import admin
from .models import Message, Gallery

# Register your models here.

admin.site.register((Message, Gallery))
