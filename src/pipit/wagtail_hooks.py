from django.templatetags.static import static
from django.utils.html import format_html
from wagtail.snippets.models import register_snippet
from wagtail import hooks
from customuser.models import User
from jobs.models import *
from wagtail.snippets.views.snippets import SnippetViewSet
# from wagtail.admin.helpers import ButtonHelper



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
    
    
#CSV Exports
# class ExportButtonHelper(ButtonHelper):
#     export_button_classnames = ['icon', 'icon-download']

#     def export_button(self, classnames_add=None, classnames_exclude=None):
#         if classnames_add is None:
#             classnames_add = []
#         if classnames_exclude is None:
#             classnames_exclude = []

#         classnames = self.export_button_classnames + classnames_add
#         cn = self.finalise_classname(classnames, classnames_exclude)
#         text = _('Export {} to CSV'.format(self.verbose_name_plural.title()))

#         return {
#             'url': self.url_helper.get_action_url('export',
#                                             query_params=self.request.GET),
#             'label': text,
#             'classname': cn,
#             'title': text,
#         }
        
# class ExportAdminURLHelper(AdminURLHelper):
#     non_object_specific_actions = ('create', 'choose_parent', 'index',
#                                     'export')

#     def get_action_url(self, action, *args, **kwargs):
#         query_params = kwargs.pop('query_params', None)

#         url_name = self.get_action_url_name(action)
#         if action in self.non_object_specific_actions:
#             url = reverse(url_name)
#         else:
#             url = reverse(url_name, args=args, kwargs=kwargs)

#         if query_params:
#             url += '?{params}'.format(params=query_params.urlencode())

#         return url

#     def get_action_url_pattern(self, action):
#         if action in self.non_object_specific_actions:
#             return self._get_action_url_pattern(action)

#         return self._get_object_specific_action_url_pattern(action)
