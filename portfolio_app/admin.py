from django.contrib import admin

from .models import Category, Project, SiteStats, Skill, UserProfile


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "is_featured")
    list_filter = ("category", "is_featured")
    search_fields = ("title", "description", "tech_stack")
    list_select_related = ("category",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ("name", "slug")


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "proficiency")
    list_filter = ("category",)
    search_fields = ("name",)


admin.site.register(SiteStats)
admin.site.register(UserProfile)
