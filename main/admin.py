from django.contrib import admin
from main import models
# Register your models here.

admin.site.register([
    models.Question,
    models.Test,
    models.Choice,
    models.TestQuestion,
])
