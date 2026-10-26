from django.core.cache import cache
from django.shortcuts import render
from .models import Category, Project, SiteStats, UserProfile, Skill


def home_view(request):
    context = cache.get('portfolio_cached_data')

    if context is None:
        categories = Category.objects.all()
        projects = Project.objects.all()
        featured_projects = Project.objects.filter(is_featured=True)[:5]
        stats = SiteStats.objects.first()
        profile = UserProfile.objects.first()
        skills = Skill.objects.all()
        context = {
            'categories': categories,
            'projects': projects,
            'featured_projects': featured_projects,
            'stats': stats,
            'profile': profile,
            'skills': skills,
        }
        
        cache.set('portfolio_cached_data', context, 900)
        print("🔄 [Cache Miss] Loaded full dataset with separate recent projects limit.")
    else:
        print("⚡ [Cache Hit] Serving instantly from RAM cache!")

    return render(request, 'portfolio_app/index.html', context)
