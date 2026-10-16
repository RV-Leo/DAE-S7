"""Queries behind the views. Part 2 of the lab happens in this file."""
from blog.models import Post


def posts_for_front_page():
    """Return published posts with their authors and tags efficiently."""
    return (
        Post.objects.filter(published=True)
        .order_by("-published_at")
        .select_related("author", "category")
        .prefetch_related("tags")
    )
