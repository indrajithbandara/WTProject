from django.contrib import admin
from .models import CredentialsModel
from .models import Course, ContactModel

# Register your models here.
admin.site.register(CredentialsModel)
admin.site.register(Course)
admin.site.register(ContactModel)