from django.contrib import admin
from .models import Post,Postcategory

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','content','created_on']

@admin.register(Postcategory)
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ['id','cat_content','created_on']