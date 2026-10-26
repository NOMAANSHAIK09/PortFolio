from django.core.cache import cache
from django.shortcuts import render
from .models import Category, Project, SiteStats, UserProfile, Skill


def home_view(request):
    context = cache.get('portfolio_cached_data')

    if context is None:
        # Convert to lists immediately so they evaluate queries cleanly before caching
        categories = list(Category.objects.all())
        
        # 1. All projects for your category folders/tabs (so full-stack, aiml, etc. work!)
        projects = list(Project.objects.all().order_by('-id'))
        
        # 2. Only the last 6 projects specifically for the bottom display grid (fixes speed)
        recent_projects = list(Project.objects.all().order_by('-id')[:6])
        
        featured_projects = list(Project.objects.filter(is_featured=True)[:5])
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