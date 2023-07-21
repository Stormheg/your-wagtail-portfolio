from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel


class HomePage(Page):
    template = "pages/home.html"


class PortfolioPage(Page):
    template = "pages/portfolio.html"


class StandardPage(Page):
    template = "pages/standard.html"


class BlogIndexPage(Page):
    template = "pages/blog_index.html"


class BlogPostPage(Page):
    template = "pages/blog_post.html"
