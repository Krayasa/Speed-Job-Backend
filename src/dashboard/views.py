
# from wagtail.admin.auth import permission_denied
# from wagtail.admin.views.reports import PageReportView
# from wagtail.models import Page

# class UnpublishedChangesReportView(PageReportView):

#     header_icon = 'doc-empty-inverse'
#     template_name = 'reports/unpublished_changes_report.html'
#     title = "Pages with unpublished changes"

#     list_export = PageReportView.list_export + ['last_published_at']
#     export_headings = dict(last_published_at='Last Published', **PageReportView.export_headings)

#     def get_queryset(self):
#         return Page.objects.filter(has_unpublished_changes=True)

#     def dispatch(self, request, *args, **kwargs):
#         if not self.request.user.is_superuser:
#             return permission_denied(request)
#         return super().dispatch(request, *args, **kwargs)