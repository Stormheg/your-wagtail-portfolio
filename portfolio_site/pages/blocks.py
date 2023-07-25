from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


# In this file we create our own blocks that can be added inside a StreamField field on a page model

class SectionBlock(blocks.StructBlock):
    heading = blocks.CharBlock(label="Heading")
    # The design of the SectionBlock does not work well if things like images or embeds are used.
    # To prevent an editor from breaking the site layout, we only allow certain rich text features to be used.
    text = blocks.RichTextBlock(
        features=["bold", "italic", "link", "or", "ul"], label="Text"
    )
    image = ImageChooserBlock(label="Image")

    class Meta:
        template = "blocks/section_block.html"


class FeaturedBlogPostItemBlock(blocks.StructBlock):
    page = blocks.PageChooserBlock(page_type="pages.BlogPostPage")


    class Meta:
        template = "blocks/featured_blog_post_item.html"


class FeaturedBlogPostListBlock(blocks.StructBlock):
    heading = blocks.CharBlock(label="Heading")
    text = blocks.TextBlock(required=False, label="Text")
    # ListBlock allows the editor to add the same block multiple times
    posts = blocks.ListBlock(FeaturedBlogPostItemBlock, label="Posts")


    class Meta:
        template = "blocks/featured_blog_post_list.html"
