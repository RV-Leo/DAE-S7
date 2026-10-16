"""YOUR answers. One function per question, no arguments.

Write the ORM query that answers each question and return it (a QuerySet or a
list). Do not write SQL and do not filter in Python what the database can
filter. Check yourself with:

    python manage.py duel                 # all of them
    python manage.py duel --question q4   # just one

Question 5 asks for two numbers per post: annotate them as `n_comments` and
`n_tags`.
"""
from datetime import date  # noqa: F401  (you will need it in question 3)

from django.db.models import Count, Q  # noqa: F401

from blog.models import Author, Category, Comment, Post, Profile, Tag  # noqa: F401


def q1():
    """Return published posts."""
    return Post.objects.filter(published=True)


def q2():
    """Return posts without a category."""
    return Post.objects.filter(category__isnull=True)


def q3():
    """Return posts published during March through May 2026, inclusive."""
    return Post.objects.filter(published_at__range=(date(2026, 3, 1), date(2026, 5, 31)))


def q4():
    """Return posts with more than two comments."""
    return Post.objects.annotate(n_comments=Count("comments")).filter(n_comments__gt=2)


def q5():
    """Return the top three published posts with comment and tag counts."""
    return (
        Post.objects.filter(published=True)
        .annotate(
            n_comments=Count("comments", distinct=True),
            n_tags=Count("tags", distinct=True),
        )
        .order_by("-n_comments")[:3]
    )


def q6():
    """Return posts written by authors from Peru, published or not."""
    return Post.objects.filter(author__profile__country="Perú")


def q7():
    """Return comments on posts in the Technology category."""
    return Comment.objects.filter(post__category__name="Tecnología")


def q8():
    """Return authors who have never published a post."""
    return Author.objects.exclude(posts__published=True)
