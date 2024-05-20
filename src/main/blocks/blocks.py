from django import forms
from django.utils.encoding import force_str
from django.utils.text import slugify

from wagtail.blocks import (
    StructBlock,
    ListBlock,
    CharBlock,
    TextBlock,
    URLBlock,
    ChoiceBlock,
    FieldBlock,
    StreamBlock

)
from wagtail.images.blocks import ImageChooserBlock
from wagtail.api import APIField
from wagtail.images.api.fields import ImageRenditionField

# from grapple.helpers import register_streamfield_block
# from grapple.models import GraphQLString, GraphQLStreamfield, GraphQLImage


class HashBlock(FieldBlock):
    """Hash values which will allow sections to be automatically linked to using URL hashes
    e.g. link to a page at a particular section could be https://your-site.com/your-page-slug/#your-section-hash
    specifically to be used to in page section rensering throught url

    Can be blank, in which case no hash should be generated for the section.

    This Block is essentially a CharBlock with a custom clean() method.
    """

    def __init__(
        self, required=True, help_text=None, max_length=None, min_length=None, **kwargs
    ):
        self.field = forms.CharField(
            required=required,
            help_text=help_text,
            max_length=max_length,
            min_length=min_length,
        )
        super().__init__(**kwargs)

    def get_searchable_content(self, value):
        return [force_str(value)]

    def clean(self, value):
        if value:
            return slugify("section-" + force_str(value), allow_unicode=False)
        return value

#@register_streamfield_block
class ButtonBlock(StructBlock):
    text = CharBlock(required=True, max_length=100, label="Text")
    link = URLBlock(required=True, label="Link")
    btntype = ChoiceBlock(
        required=True,
        choices=[
            ("primary", "Primary"),
            ("secondary", "Secondary")
        ]
    )

    api_fields = [APIField("text"), APIField("link"),APIField("btntype")]

#@register_streamfield_block
class HeroSection(StructBlock):
    heading = TextBlock(
        required=False,
        label="Hero title",
        default="Manpower Service from a ISO Certified Recruitment Agency",
    )

    description = TextBlock(
        required=False,
        label="Hero subtitle",
        default="The thing we do is take care of your human reosurces",
    )
    image = ImageChooserBlock(required=False, label="Hero image")
    button=ButtonBlock(required=False,label="CTA")
    hash = HashBlock(
        required=False,
        max_length=80,
        label="Hash",
        help_text="Allow navigation to this section within a page. e.g. 'team' allows navigation to /http://your-site.com/#team",
    )

    api_fields = [
        APIField("heading"),
        APIField("description"),
        APIField("image"),
        APIField("button"),
        APIField("hash"),
    ]

    class Meta:
        icon = "placeholder"
        label = "Hero Section"

#@register_streamfield_block
class TeamMemberBlock(StructBlock):
    name = CharBlock(required=True, max_length=255, label="Name")
    image = ImageChooserBlock(required=False, label="Photo")
    role = CharBlock(required=True, max_length=255, label="Role / Job Title")
    biography = TextBlock(required=False, label="Bio")
    linkedin = URLBlock(required=False, label="LinkedIn Page")
    twitter = URLBlock(required=False, label="Twitter Page")

    api_fields = [
        APIField("name"),
        APIField("image"),
        APIField("role"),
        APIField("biography"),
        APIField("linkedin"),
        APIField("twitter"),

    ]

    class Meta:
        icon = "user"
        label = "Team Member"

#@register_streamfield_block
class TeamSection(StructBlock):
    heading = TextBlock(
        required=False,
        label="Heading",
        default="Our illustrious leaders",
    )
    description = TextBlock(
        required=False,
        label="Description",
        default="Here is a list of our Head Peeps. They look glorious rendered in HTML but are probably just normal, mortal humans.",
    )
    members = ListBlock(TeamMemberBlock(),required=False,label="Team Members")
    hash = HashBlock(
        required=False,
        max_length=80,
        label="Hash",
        help_text="Allow navigation to this section within a page. e.g. 'team' allows navigation to /http://your-site.com/#team",
    )

    api_fields = [
        APIField("heading"),
        APIField("description"),
        APIField("members"),
        APIField("hash"),
    ]

    class Meta:
        icon = "group"
        label = "Team Section"

#@register_streamfield_block
class CarouselImageBlock(StructBlock):
    image = ImageChooserBlock()
    heading = TextBlock(
            required=False,
            label="Main text",
            help_text="Add an image subtitle",
        )

    description =TextBlock(
            required=False,
            label="Description",
            help_text="Add some descriptive information with your image",
        )

    api_fields = [
        APIField("image"),
        APIField("description"),
        APIField("heading"),
        ]
    class Meta:
        icon = "image"
        label = "Carousel Image"

#@register_streamfield_block
class CarouselSection(StructBlock):
    heading = TextBlock(
            required=False,
            label="Heading",
            help_text="Add a heading at the beginning of this page section",
        )
    description = TextBlock(
        required=False,
        label="Description",
        help_text="Provide a slightly more detailed description of what this carousel section is for",
    )
    images = ListBlock(CarouselImageBlock(), label="Images")
    hash = HashBlock(
        required=False,
        max_length=80,
        label="Hash",
        help_text="Allow navigation to this section within a page. e.g. 'team' allows navigation to /http://your-site.com/#team",
    )
    api_fields = [
        APIField("heading"),
        APIField("description"),
        APIField("images"),
        APIField("hash"),
    ]

    class Meta:
        icon = "image"
        label = "Carousel Section"

#@register_streamfield_block
class FaqBlock(StructBlock):
    question = TextBlock(
        required=True,
        label="Question",
        help_text="Add a simply worded question, like 'How much will it cost?'",
    )
    answer = TextBlock(
        required=True,
        label="Answer",
        help_text="Provide a short answer in no more than a few lines of text",
    )
    button = ButtonBlock(
        required=False,
        label="Button",
        help_text="Add a link to be followed for more information on that question, feature or product",
    )
    api_fields = [
        APIField("question"),
        APIField("answer"),
        APIField("button"),
    ]
    class Meta:
        icon = "help"
        label = "FAQ"

#@register_streamfield_block
class FaqSection(StructBlock):
    heading =TextBlock(
            required=False,
            label="Heading",
            help_text="Add a heading at the beginning of this page section",
        )
    description = TextBlock(required=False, label="Description")
    hash = HashBlock(
        required=False,
        max_length=80,
        label="Hash",
        help_text="Allow navigation to this section within a page. e.g. 'team' allows navigation to /http://your-site.com/#team",
    )
    faqs = ListBlock(FaqBlock(), label="FAQs")

    api_fields = [
        APIField("heading"),
        APIField("description"),
        APIField("faqs"),
        APIField("hash"),
    ]
    class Meta:
        icon = "help"
        label = "FAQs Section"


#@register_streamfield_block
class TestimonialBlock(StructBlock):
    name = CharBlock(
        required=True,
        max_length=255,
        label="Name",
        help_text="Name of the person making the recommendation",
    )
    role = CharBlock(
        required=False,
        max_length=255,
        label="Role",
        help_text="Job title of the person making the recommentation, if any",
    )
    organisation = TextBlock(
        required=False,
        label="Organisation",
        help_text="Name of the organisation the person is part of, if any",
    )
    quote = TextBlock(
        required=True,
        label="Quote",
        help_text="The nice things they have to say",
    )
    image = ImageChooserBlock(
        required=False,
        label="Logo/Picture",
        help_text="Add either a company logo or a person's mugshot",
    )
    stars = ChoiceBlock(
        required=True,
        choices=[
            (None, "No rating"),
            (0, "0 Stars"),
            (1, "1 Star"),
            (2, "2 Stars"),
            (3, "3 Stars"),
            (4, "4 Stars"),
            (5, "5 Stars"),
        ],
        icon="pick",
    )

    api_fields = [
        APIField("name"),
        APIField("role"),
        APIField("organisation"),
        APIField("quote"),
        APIField("stars"),
        APIField("image"),
    ]

    class Meta:
        icon = "pick"
        label = "Testimonial"


#@register_streamfield_block
class TestimonialSection(StructBlock):
    heading = TextBlock(
        required=False,
        label="Heading",
        default="Testimonials",
        help_text="Add a heading at the beginning of this page section",
    )
    description = TextBlock(
        required=False,
        label="Description",
        default="Our users love us. Look at these rave reviews...",
    )
    hash = HashBlock(
        required=False,
        max_length=80,
        label="Hash",
        help_text="Allow navigation to this section within a page. e.g. 'team' allows navigation to /http://your-site.com/#team",
    )
    testimonials = ListBlock(TestimonialBlock())


    api_fields = [
        APIField("heading"),
        APIField("description"),
        APIField("hash"),
        APIField("testimonials"),
    ]

    class Meta:
        icon = "pick"
        label = "Testimonials Section"


#@register_streamfield_block
class FeatureBlock(StructBlock):
    heading = TextBlock(
        required=True,
        label="Feature",
        help_text="Feature name. Keep it short, like 'Free Chat' or 'Secure'",
    )
    description = TextBlock(
        required=True,
        label="Description",
        help_text="Write a few lines about this feature",
    )
    image=ImageChooserBlock(required=False)
    button=ButtonBlock(required=False)

    api_fields = [
        APIField("heading"),
        APIField("description"),
        APIField("image"),
        APIField("button"),
    ]

    class Meta:
        icon = "tick-inverse"
        label = "Product Feature Description"


#@register_streamfield_block
class FeatureRowSection(StructBlock):
    heading =TextBlock(
            required=False,
            label="Heading",
            default="Why our product is best",
            help_text="Add a heading at the beginning of this page section",
        )
    description = TextBlock(
        required=False,
        label="Description",
        help_text="This is the paragraph where you can write more details about your product. Keep it meaningful!",
    )
    longdescription = TextBlock(
        required=False,
        label="Long Description",
        help_text="This is the paragraph where you can write more details about your product. Keep it meaningful!",
    )
    image = ImageChooserBlock(
        required=False,
        label="Image",
        help_text="Pick an image for the side panel of a feature list",
    )
    features = ListBlock(FeatureBlock(), label="Features")
    hash = HashBlock(
        required=False,
        max_length=80,
        label="Hash",
        help_text="Allow navigation to this section within a page. e.g. 'team' allows navigation to /http://your-site.com/#team",
    )


    api_fields = [
        APIField("heading"),
        APIField("description"),
        APIField("longdescription"),
        APIField("image"),
        APIField("hash"),
        APIField("features"),
    ]


    class Meta:
        icon = "list-ul"
        label = "Brand Features Row Section"

#@register_streamfield_block
class FeatureSection(StructBlock):
    heading =TextBlock(
            required=False,
            label="Heading",
            default="Why our product is best",
            help_text="Add a heading at the beginning of this page section",
        )
    # description = TextBlock(
    #     required=False,
    #     label="Description",
    #     help_text="This is the paragraph where you can write more details about your product. Keep it meaningful!",
    # )

    # image = ImageChooserBlock(
    #     required=False,
    #     label="Image",
    #     help_text="Pick an image for the side panel of a feature list",
    # )
    features = ListBlock(FeatureBlock(), label="Features")
    hash = HashBlock(
        required=False,
        max_length=80,
        label="Hash",
        help_text="Allow navigation to this section within a page. e.g. 'team' allows navigation to /http://your-site.com/#team",
    )


    api_fields = [
        APIField("heading"),
        # APIField("description"),
        # APIField("image"),
        APIField("hash"),
        APIField("features"),
    ]


    class Meta:
        icon = "list-ul"
        label = "Brand Features Section"


#@register_streamfield_block
class LogoCloudBlock(StructBlock):
    country = TextBlock(
        required=False,
        label="Country Name",
        default="Nepal",
        help_text="Add a country name",
    )

    image = ImageChooserBlock(
        required=False,
        label="Image",
        help_text="Pick an image for the country logo",
    )

    api_fields = [
        APIField("country"),
        APIField("image"),
    ]

    class Meta:
        icon = "list-ul"
        label = "Logos"


#@register_streamfield_block
class LogoCloudSection(StructBlock):
    description = TextBlock(
        required=False,
        label="Description",
        default="We serve in 17 countries",
        help_text="Add a description",
    )

    countries = ListBlock(LogoCloudBlock(), label = "Countries")

    api_fields = [
        APIField("description"),
        APIField("countries"),
    ]

    class Meta:
        icon = "pick"
        label = "Logo Section"


#@register_streamfield_block
class ArticleBlock(StructBlock):
    image = ImageChooserBlock(
        required=False,
        label="Image",
        help_text="Pick an image for blog",
    )

    category = ChoiceBlock(
        required=True,
        choices=[
            ("construction", "Construction"),
            ("manpower", "Manpower"),
        ],
        icon="pick",
    )
    
    heading = TextBlock(
        required=False,
        label="Title",
        default="Manpower",
        help_text="Add a title",
    )

    description = TextBlock(
        required=False,
        label="Description",
        default="Manpower",
        help_text="Add a description",
    )

    api_fields = [
        APIField("image"),
        APIField("category"),
        APIField("heading"),
        APIField("description"),
    ]

    class Meta:
        icon = "list-ul"
        label = "Article Block"


#@register_streamfield_block
class ArticleSection(StructBlock):
    heading = TextBlock(
        required=False,
        label="Title",
        default="From the blog",
        help_text="Add a title",
    )

    description = TextBlock(
        required=False,
        label="Description",
        default="Learn how to grow your business with our expert advice",
        help_text="Add a description",
    )

    articles = ListBlock(ArticleBlock(), label = "Articles")

    api_fields = [
        APIField("heading"),
        APIField("description"),
        APIField("articles"),
    ]

    class Meta:
        icon = "pick"
        label = "Article Section"


#@register_streamfield_block
class ContactSection(StructBlock):
    heading =TextBlock(
            required=False,
            label="Heading",
            default="Ready To Take The Next Step?",
            help_text="Add a heading at the beginning of this page section",
        )
    description = TextBlock(
        required=False,
        label="Description",
        help_text="This is the paragraph where you can write more details. Keep it meaningful!",
    )
    location1 = TextBlock(
        required=False,
        label="Location 1",
        help_text="Write your address",
    )
    location2 = TextBlock(
        required=False,
        label="Location 2",
        help_text="Write Country and district",
    )
    phone = TextBlock(
        required=False,
        label="Phone Number",
        help_text="Write Number",
    )
    email = TextBlock(
        required=False,
        label="Email",
        help_text="Write email",
    )
    button=ButtonBlock(required=False)


    api_fields = [
        APIField("heading"),
        APIField("description"),
        APIField("location1"),
        APIField("location2"),
        APIField("phone"),
        APIField("email"),
        APIField("button"),
    ]


    class Meta:
        icon = "user"
        label = "Contact Section"


#@register_streamfield_block
class JobFormSection(StructBlock):
    heading =TextBlock(
            required=False,
            label="Title",
            default="Job Title",
            help_text="Add a title for the job",
        )
    description = TextBlock(
        required=False,
        label="Description",
        help_text="This is the paragraph where you can write more details about jobs.",
    )

    button = ButtonBlock(required=True)


    api_fields = [
        APIField("heading"),
        APIField("description"),
        APIField("button"),
    ]


    class Meta:
        icon = "user"
        label = "Job Form Section"

