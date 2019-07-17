from django.contrib import admin
from .models import Study_material,Homework,Syllabus,Post,Upload_assignment
admin.site.register(Study_material)
admin.site.register(Homework)
admin.site.register(Syllabus)
admin.site.register(Post)
admin.site.register(Upload_assignment)
admin.site.site_header ='Administration'
