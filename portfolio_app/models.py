from django.db import models


class UserProfile(models.Model):
    name = models.CharField(max_length=100, default="Alex Morgan")
    title = models.CharField(max_length=200, default="AI/ML Architect & Backend Dev")
    bio = models.TextField(default="Specializing in Deep Learning, LLM pipelines, and scalable architectures.")
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True) # Or use a URLField if easier
    skills_list = models.CharField(max_length=300, default="Python, PyTorch, Django, React, TensorFlow")

    def __str__(self):
        return f"Profile: {self.name}"
    
class Category(models.Model):
    name = models.CharField(max_length=50) # e.g., AI/ML, Full Stack
    slug = models.SlugField(unique=True)   # e.g., aiml, webdev

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='projects')
    description = models.TextField()
    tech_stack = models.CharField(max_length=200) # e.g., PyTorch, Django, Tailwind
    live_demo_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    is_featured = models.BooleanField(default=False) # For your Top 5 projects

    def __str__(self):
        return self.title

class SiteStats(models.Model):
    leetcode_solved = models.IntegerField(default=450)
    total_projects_done = models.IntegerField(default=30)
    github_contributions = models.IntegerField(default=1200)

    def __str__(self):
        return "Live Portfolio Metrics"
    
class Skill(models.Model):
    SKILL_CATEGORIES = [
        ('aiml', 'AI / ML & Data Science'),
        ('backend', 'Backend & APIs'),
        ('frontend', 'Frontend & UI'),
        ('tools', 'DevOps & Tools'),
    ]
    
    name = models.CharField(max_length=50) # e.g., PyTorch, Django, Docker
    category = models.CharField(max_length=20, choices=SKILL_CATEGORIES, default='aiml')
    proficiency = models.IntegerField(default=85) # Percentage, e.g. 90 for 90%
    
    def __str__(self):
        return f"{self.name} ({self.proficiency}%)"