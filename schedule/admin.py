from django.contrib import admin
from .models import *

admin.site.register(Teacher)
admin.site.register(TrainingSession)
admin.site.register(ClassRoom)
admin.site.register(Group)
admin.site.register(Schedule)