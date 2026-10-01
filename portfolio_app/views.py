from django.shortcuts import render
from .models import Project, Category, SiteStats, UserProfile

def home_view(request):
    categories = Category.objects.all()
    projects = Project.objects.all()
    featured_projects = Project.objects.filter(is_featured=True)[:5]
    stats = SiteStats.objects.first()
    profile = UserProfile.objects.first()
    context = {
        'categories': categories,
        'projects': projects,
        'featured_projects': featured_projects,
        'stats': stats,
        'profile': profile,
    }
    return render(request, 'portfolio_app/index.html', context)