from django.templatetags.static import static
from django.utils.html import format_html
from wagtail.snippets.models import register_snippet
from wagtail import hooks
from customuser.models import User
from jobs.models import *
from wagtail.snippets.views.snippets import SnippetViewSet


class UserViewSet(SnippetViewSet):
    model = User
    icon = "user"
    menu_label = "Users"
    menu_name = "users"
    menu_order = 300
    add_to_admin_menu = True
    
class JobViewSet(SnippetViewSet):
    model = Job
    icon = "tag"
    menu_label = "Jobs"
    menu_name = "jobs"
    menu_order = 300
    add_to_admin_menu = True
    
class ApplicantViewSet(SnippetViewSet):
    model = Applicant
    icon = "group"
    menu_label = "Applicants"
    menu_name = "applicant"
    menu_order = 300
    add_to_admin_menu = True
    
class FavoriteViewSet(SnippetViewSet):
    model = Favorite
    icon = "plus"
    menu_label = "Favorites"
    menu_name = "favorites"
    menu_order = 300
    add_to_admin_menu = True

register_snippet(UserViewSet)
register_snippet(JobViewSet)
register_snippet(ApplicantViewSet)
register_snippet(FavoriteViewSet)

@hooks.register("insert_global_admin_css")
def insert_global_admin_css():
    return format_html(
        '<link rel="stylesheet" type="text/css" href="{}">',
        static("pipit/admin-overrides.css"),
    )
    
