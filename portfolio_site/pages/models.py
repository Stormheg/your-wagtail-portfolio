from django.db import models
from django.core.paginator import Paginator

from wagtail.models import Page, Orderable, ParentalKey
from wagtail.fields import StreamField, RichTextField
from wagtail.search import index
from wagtail.snippets.models import register_snippet
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel


# Import all the block types we defined in blocks.py
from portfolio_site.pages import blocks


@register_snippet
class Skill(models.Model):
    name = models.CharField("name", max_length=16)

    def __str__(self):
        return self.name


class HomePageSkillPlacement(Orderable, models.Model):
    """This model defines a relation between the Skill snippet and the HomePage.

    It tells Django that skills can be placed on the home page.

    We use Wagtails' Orderable class to allow the Skills to be reordered in the Wagtail admin.
    """

    # A skill
    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE,
    )
    # Can be placed on the HomePage
    page = ParentalKey(
        "pages.HomePage", on_delete=models.CASCADE, related_name="skills"
    )


class HomePage(Page):
    template = "pages/home.html"

    your_name = models.CharField("your name", max_length=32)
    headline = models.CharField("headline", max_length=92)
    subtext = models.TextField("subtext")
    image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.PROTECT,  # Prevent the image this this field is referencing from being deleted
        verbose_name="image",
    )
    button_label = models.CharField("button label", max_length=32, blank=True)
    button_page = models.ForeignKey(
        "wagtailcore.Page",
        on_delete=models.SET_NULL,  # When the page this field is referencing is deleted, clear the field
        null=True,
        verbose_name="button page",
        related_name="+",
    )

    # All the other content on the page is contained in a StreamField
    # StreamFields allow you to use your own blocks in any order you like, as many as you want
    # This feature is what people are usually most excited about in Wagtail!
    body = StreamField(
        block_types=[
            ("section", blocks.SectionBlock()),
            ("featured_blog_posts", blocks.FeaturedBlogPostListBlock()),
        ],
        use_json_field=True,
        null=True,
        verbose_name="body",
    )

    # Wagtail looks for a field called 'content_panels' when editing a page
    # This field controls what other fields can be edited through Wagtail's page editor interface.
    content_panels = Page.content_panels + [
        # MultiFieldPanel groups all fields visually in the Wagtail admin
        MultiFieldPanel(
            [
                FieldPanel("your_name"),
                FieldPanel("headline"),
                FieldPanel("subtext"),
                FieldPanel("image"),
                FieldPanel("button_label"),
                FieldPanel("button_page"),
                InlinePanel("skills", heading="Skills"),
            ],
            heading="Headline",
        ),
        FieldPanel("body"),
    ]


class PortfolioPage(Page):
    template = "pages/portfolio.html"


class StandardPage(Page):
    template = "pages/standard.html"


class BlogIndexPage(Page):
    template = "pages/blog_index.html"

    def get_context(self, request, *args, **kwargs):
        # get_context allows us to pass extra data to the template. This is called 'context'.

        # Wagtail already adds context for us. We must call this method to ensure we also pass Wagtail's context to the template.
        context = super().get_context(request, *args, **kwargs)

        # Get all blog post pages that are children of the blog index and order them by descending date (newer posts first)
        blog_posts = BlogPostPage.objects.child_of(self).order_by("-date")

        # Add a 'blog_posts' variable that we can use in the template
        context["blog_posts"] = blog_posts
        return context


class BlogPageGalleryImage(Orderable):
    page = ParentalKey(
        "pages.BlogPostPage", on_delete=models.CASCADE, related_name="gallery_images"
    )
    image = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.CASCADE, related_name="+"
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel("image"),
        FieldPanel("caption"),
    ]


class BlogPostPage(Page):
    template = "pages/blog_post.html"

    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField("intro"),
        index.SearchField("body"),
    ]

    content_panels = Page.content_panels + [
        FieldPanel("date"),
        FieldPanel("intro"),
        FieldPanel("body"),
        InlinePanel("gallery_images", label="Gallery images"),
    ]
