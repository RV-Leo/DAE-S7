"""Queries behind the views. Part 2 of the lab happens in this file."""
from blog.models import Post


def posts_for_front_page():
    """Return published posts ordered by most recent, using select_related and
    prefetch_related to solve the N+1 problem.

    Without these optimisations the template triggers one query per post to
    fetch ``post.author`` and one query per post to fetch ``post.tags``.
    With ``select_related("author")`` the author is fetched in the first query
    and ``prefetch_related("tags")`` loads all tags in a second query, bringing
    the total from ``2 * N + 1`` down to exactly **2 queries**.
    """
    return (
        Post.objects.order_by("-published_at")
        .select_related("author")
        .prefetch_related("tags")
    )
