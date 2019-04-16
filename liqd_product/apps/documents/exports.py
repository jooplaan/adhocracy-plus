from django.utils.translation import ugettext as _
from rules.contrib.views import PermissionRequiredMixin

from adhocracy4.comments.models import Comment
from adhocracy4.exports import mixins as export_mixins
from adhocracy4.exports import views as export_views
from liqd_product.apps.exports import mixins as mb_export_mixins


class DocumentExportView(
        PermissionRequiredMixin,
        export_mixins.ExportModelFieldsMixin,
        mb_export_mixins.UserGeneratedContentExportMixin,
        export_mixins.ItemExportWithLinkMixin,
        export_mixins.ItemExportWithRatesMixin,
        mb_export_mixins.ItemExportWithRepliesToMixin,
        export_views.BaseItemExportView
):

    model = Comment
    permission_required = 'liqd_product_documents.change_chapter'

    fields = ['id', 'comment', 'created']

    def get_permission_object(self):
        return self.module

    def get_queryset(self):
        comments = (
            Comment.objects.filter(paragraph__chapter__module=self.module) |
            Comment.objects.filter(chapter__module=self.module) |
            Comment.objects.filter(
                parent_comment__paragraph__chapter__module=self.module) |
            Comment.objects.filter(parent_comment__chapter__module=self.module)
        )
        return comments

    def get_virtual_fields(self, virtual):
        virtual.setdefault('id', _('ID'))
        virtual.setdefault('comment', _('Comment'))
        virtual.setdefault('created', _('Created'))
        return super().get_virtual_fields(virtual)

    @property
    def raise_exception(self):
        return bool(self.request.user.is_authenticated)