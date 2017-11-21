from django.contrib import admin

from .models import Ingredient, Product, Recipy, Comment,Fridge

class IngredientInline(admin.StackedInline):
    model = Ingredient
    extra = 3

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1

class RecipyAdmin(admin.ModelAdmin):
    inlines = [IngredientInline, CommentInline]

admin.site.register(Ingredient)
admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(Recipy, RecipyAdmin)
admin.site.register(Fridge)
