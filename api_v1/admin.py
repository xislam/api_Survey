from django.contrib import admin

# Register your models here.
from api_v1.models import *

admin.site.register(Survey)
admin.site.register(Questions)
admin.site.register(Choice)
admin.site.register(Answer)
