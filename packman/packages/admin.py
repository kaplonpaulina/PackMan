from django.contrib import admin
from packages.models import Package
# Register your models here.

from django.apps import AppConfig

class BasicAppConfig(AppConfig):
	name = 'packages'

	
admin.site.register(Package)