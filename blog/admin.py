from django.contrib import admin

from .models import Author, Category, Comment, Post, Profile, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "category", "published", "published_at")
    list_filter = ("published", "category")
    search_fields = ("title",)

    def get_queryset(self, request):
        # Show all posts (including drafts) in the admin
        return Post.all_objects.order_by("-published_at")


admin.site.register([Author, Profile, Category, Tag, Comment])
