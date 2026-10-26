from django.core.cache import cache
from django.shortcuts import render
from .models import Category, Project, SiteStats, UserProfile, Skill

def home_view(request):
    # Try to get cached data for blazing fast speed ⚡
    context = cache.get('portfolio_cached_data')

    if context is None:
        categories = list(Category.objects.all())
        
        # 1. ALL projects so your category folders/tabs show everything correctly!
        projects = list(Project.objects.all().order_by('-id'))
        
        # 2. ONLY the last 6 projects specifically for the bottom display section
        recent_projects = list(Project.objects.all().order_by('-id')[:6])
        
        featured_projects = list(Project.objects.filter(is_featured=True)[:5])
        stats = SiteStats.objects.first()
        profile = UserProfile.objects.first()
        skills = list(Skill.objects.all())

        context = {
            'categories': categories,
            'projects': projects,                 # Used for category filtering folders
            'recent_projects': recent_projects,   # Used for the bottom 6-project grid
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