from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(ItecUser)
admin.site.register(Group)
admin.site.register(Profile)
admin.site.register(Task)
admin.site.register(Gradebook)
admin.site.register(GradebookRecord)
