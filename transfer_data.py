import os
import django
import json
from django.core.serializers import serialize

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_portfolio.settings')
django.setup()

from portfolio_app.models import Category, Project, SiteStats, UserProfile, Skill

def export_json():
    print("📦 Exporting database data to JSON with UTF-8 encoding...")
    
    # Gather all models from your app
    data = list(Category.objects.all()) + \
           list(Project.objects.all()) + \
           list(SiteStats.objects.all()) + \
           list(UserProfile.objects.all()) + \
           list(Skill.objects.all())

    # Serialize to JSON format natively
    serialized_data = serialize('json', data, use_natural_foreign_keys=True, use_natural_primary_keys=True)
    
    # Write directly using UTF-8 encoding (avoids Windows charmap errors)
    with open('portfolio_data.json', 'w', encoding='utf-8') as f:
        f.write(serialized_data)
        
    print("✅ Successfully exported data to portfolio_data.json!")

if __name__ == '__main__':
    export_json()