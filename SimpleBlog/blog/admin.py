from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(PostCetgory)


admin.site.site_header = 'Simple Blog'    