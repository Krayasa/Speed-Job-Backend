from django import forms
from django.utils.encoding import force_str
from django.utils.text import slugify
from django.db import models
from django.core.exceptions import ValidationError

from wagtail.blocks import (
    StructBlock,
    ListBlock,
    CharBlock,
    TextBlock,
    URLBlock,
    ChoiceBlock,
    FieldBlock,
    StreamBlock,
    PageChooserBlock,
    RichTextBlock,

)
from wagtail.images.blocks import ImageChooserBlock
from wagtail.api import APIField

class APIImageChooserBlock(ImageChooserBlock):
    def get_api_representation(self, value, context=None):
        if value:
            return {
                'id': value.id,
                'url': value.file.url,
                'width': value.width,
                'height': value.height,
            }


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


class ButtonBlock(StructBlock):
    text = CharBlock(required=True, max_length=100, label="Text", default="Learn More")
    link = URLBlock(required=False, label="Link", default="www.speedwingshr.com")
    page = PageChooserBlock(required=False)
    btntype = ChoiceBlock(
        required=False,
        choices=[
            ("primary", "Primary"),
            ("secondary", "Secondary")
        ]
    )
    def clean(self, value):
        cleaned_data = super().clean(value)
        link = cleaned_data.get('link')
        page = cleaned_data.get('page')

        if not link and not page:
            raise ValidationError('Either "Link" or "Page" must be provided.')

        return cleaned_data

    class Meta:
        icon = "placeholder"


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
    image = APIImageChooserBlock(required=False, label="Hero image")


    button=ButtonBlock(required=False,label="CTA")
    hash = HashBlock(
        required=False,
        max_length=80,
        label="Hash",
        help_text="Allow navigation to this section within a page. e.g. 'team' allows navigation to /http://your-site.com/#team",
    )

    class Meta:
        icon = "placeholder"
        label = "Hero Section"


class TeamMemberBlock(StructBlock):
    name = CharBlock(required=True, max_length=255, label="Name")
    image = APIImageChooserBlock(required=False, label="Photo")
    role = CharBlock(required=True, max_length=255, label="Role / Job Title")
    biography = TextBlock(required=False, label="Bio")
    linkedin = URLBlock(required=False, label="LinkedIn Page")
    twitter = URLBlock(required=False, label="Twitter Page")


    class Meta:
        icon = "user"
        label = "Team Member"


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


    class Meta:
        icon = "group"
        label = "Team Section"


class CarouselImageBlock(StructBlock):
    image = APIImageChooserBlock()
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

    class Meta:
        icon = "image"
        label = "Carousel Image"


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

    class Meta:
        icon = "image"
        label = "Carousel Section"


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

    class Meta:
        icon = "help"
        label = "FAQ"


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

    class Meta:
        icon = "help"
        label = "FAQs Section"


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
    image = APIImageChooserBlock(
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

    class Meta:
        icon = "pick"
        label = "Testimonial"



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

    class Meta:
        icon = "pick"
        label = "Testimonials Section"



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
    image=APIImageChooserBlock(required=False)
    button=ButtonBlock(required=False)

    class Meta:
        icon = "tick-inverse"
        label = "Product Feature Description"



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
    image = APIImageChooserBlock(
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

    class Meta:
        icon = "list-ul"
        label = "Brand Features Row Section"


class FeatureSection(StructBlock):
    heading =TextBlock(
            required=False,
            label="Heading",
            default="Why our product is best",
            help_text="Add a heading at the beginning of this page section",
        )

    features = ListBlock(FeatureBlock(), label="Features")
    hash = HashBlock(
        required=False,
        max_length=80,
        label="Hash",
        help_text="Allow navigation to this section within a page. e.g. 'team' allows navigation to /http://your-site.com/#team",
    )

    class Meta:
        icon = "list-ul"
        label = "Brand Features Section"



class LogoCloudBlock(StructBlock):
    country = TextBlock(
        required=False,
        label="Country Name",
        default="Nepal",
        help_text="Add a country name",
    )

    image = APIImageChooserBlock(
        required=False,
        label="Image",
        help_text="Pick an image for the country logo",
    )

    class Meta:
        icon = "list-ul"
        label = "Logos"



class LogoCloudSection(StructBlock):
    description = TextBlock(
        required=False,
        label="Description",
        default="We serve in 17 countries",
        help_text="Add a description",
    )

    countries = ListBlock(LogoCloudBlock(), label = "Countries")

    class Meta:
        icon = "pick"
        label = "Logo Section"



class ArticleBlock(StructBlock):
    image = APIImageChooserBlock(
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


    class Meta:
        icon = "list-ul"
        label = "Article Block"



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

    class Meta:
        icon = "pick"
        label = "Article Section"



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

    class Meta:
        icon = "user"
        label = "Contact Section"



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

    class Meta:
        icon = "user"
        label = "Job Form Section"
        
# class ArticleSection(StructBlock):
    # image = APIImageChooserBlock(
    #     required=False,
    #     label="Image",
    #     help_text="Pick an image for blog",
    # )
    # title = TextBlock(
    #     required=False,
    #     label="Title",
    #     default="Article Title",
    #     help_text="Add an article title",
    # )
    # content = TextBlock(
    #     required=False,
    #     label="Content",
    #     help_text="Write content for the article",
    # )
    
    # article = RichTextBlock(required=True, label="Article", help_text="Write content for the article")

    # class Meta:
    #     icon = "pick"
    #     label = "Article Section"

