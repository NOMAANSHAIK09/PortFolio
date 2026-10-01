from django.contrib import admin

# Register your models here.
from .models import Category, Project, SiteStats, UserProfile

admin.site.register(Category)
admin.site.register(Project)
admin.site.register(SiteStats)
admin.site.register(UserProfile)
