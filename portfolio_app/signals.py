from django.db.backends.signals import connection_created
from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Category, Project, SiteStats, UserProfile, Skill

# Clear cache whenever any portfolio model is saved or deleted in admin
@receiver([post_save, post_delete], sender=Project)
@receiver([post_save, post_delete], sender=Category)
@receiver([post_save, post_delete], sender=SiteStats)
@receiver([post_save, post_delete], sender=UserProfile)
@receiver([post_save, post_delete], sender=Skill)
def clear_portfolio_cache(sender, **kwargs):
    cache.delete('portfolio_cached_data')
    print("🧹 Portfolio cache cleared due to admin update.")