from django.core.cache import cache
from django.shortcuts import render
from .models import Category, Project, SiteStats, UserProfile, Skill


def home_view(request):
    context = cache.get('portfolio_cached_data')

    if context is None:
        # Evaluate once and fetch each project's category in the same query.
        categories = list(Category.objects.all())
        projects = list(Project.objects.select_related('category').order_by('-id'))
        recent_projects = projects[:6]
        featured_projects = [project for project in projects if project.is_featured][:5]
        stats = SiteStats.objects.first()
        profile = UserProfile.objects.first()
        skills = list(Skill.objects.all())

        context = {
            'categories': categories,
            'projects': projects,                 # Powers your folder filters/tabs
            'recent_projects': recent_projects,   # Powers the limited bottom 6-project grid
            'featured_projects': featured_projects,
            'stats': stats,
            'profile': profile,
            'skills': skills,
        }
        
        # Cache for 15 minutes
        cache.set('portfolio_cached_data', context, 900)
        print("🔄 [Cache Miss] Loaded full dataset with separate recent projects limit.")
    else:
        print("⚡ [Cache Hit] Serving instantly from RAM cache!")

    return render(request, 'portfolio_app/index.html', context)
