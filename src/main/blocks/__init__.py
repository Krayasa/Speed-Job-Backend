from .blocks import ArticleSection, CarouselSection, ContactSection, FeatureRowSection,FeatureSection,FaqSection,HeroSection, JobFormSection, LogoCloudSection,TeamSection,TestimonialSection  # noqa

# noqa avoids "unused imports in __init__.py" error when using flake8


# Simply add this to any existing list of streamfield s in a content panel to enable creation of sections
section_blocks = [
    ("carousel_section", CarouselSection()),
    ("faq_section", FaqSection()),
    ("feature_section", FeatureSection()),
    ("hero_section", HeroSection()),
    ("team_section", TeamSection()),
    ("testimonial_section", TestimonialSection()),
    ("logo_cloud_section", LogoCloudSection()),
    ("article_section", ArticleSection()),
    ("contact_section", ContactSection()), 
    ("feature_row_section", FeatureRowSection()), 
    ("job_form_section", JobFormSection())
]
