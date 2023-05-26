from django.contrib import admin
from .models import *



class RecipeAdmin(admin.ModelAdmin):
    fieldsets = (
        ('General Information', {
            'fields': ('recipe_name', 'recipe_image', 'prep_time', 'serves', 'type', 'ingredient', 'description', 'publish'),
        }),
        ('Visualization', {
            'fields': ('custom_visualization',),
        }),
    )

    def custom_visualization(self, obj):
        # Perform custom logic to generate a visualization
        return "Custom Visualization"

class RegistrationAdmin(admin.ModelAdmin):
    fieldsets = (
        ('General Information', {
            'fields': ('name', 'email', 'password', 'chef', 'pic'),
        }),
        ('Visualization', {
            'fields': ('custom_visualization',),
        }),
    )

    def custom_visualization(self, obj):
        # Perform custom logic to generate a visualization
        return "Custom Visualization"

# Register your models here.
admin.site.register(login)
admin.site.register(registration)
admin.site.register(Recipe)
admin.site.register(SavedRecipe)
admin.site.register(Rating)