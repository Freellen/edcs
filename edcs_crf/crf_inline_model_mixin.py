import abc
from datetime import datetime

from django.core.exceptions import ImproperlyConfigured
from django.db import models
from django.db.models import ForeignKey, OneToOneField, options
from edc_sites.models import SiteModelMixin
from edcs_visit_schedule.model_mixins.crfs import InlineVisitMethodsModelMixin
from edcs_visit_schedule.stubs import SubjectVisitModelStub, TSubjectVisitModelStub

options.DEFAULT_NAMES = options.DEFAULT_NAMES + ("crf_inline_parent",)


class CrfInlineModelMixin(InlineVisitMethodsModelMixin, SiteModelMixin, models.Model):
    """A mixin for models used as inlines in ModelAdmin."""

    def __init__(self, *args, **kwargs) -> None:
        """Try to detect the inline parent model attribute
        name or raise.
        """
        super().__init__(*args, **kwargs)
        try:
            self._meta.crf_inline_parent
        except AttributeError:
            fks = [
                field
                for field in self._meta.fields
                if isinstance(field, (OneToOneField, ForeignKey))
            ]
            if len(fks) == 1:
                self.__class__._meta.crf_inline_parent = fks[0].name
            else:
                raise ImproperlyConfigured(
                    "CrfInlineModelMixin cannot determine the "
                    "inline parent model name. Got more than one foreign key. "
                    "Try declaring \"crf_inline_parent = '<field name>'\" "
                    "explicitly in Meta."
                )

    def __str__(self) -> str:
        return str(self.parent_instance.subject_visit)

    @abc.abstractmethod
    def natural_key(self) -> tuple:
        return tuple()

    @property
    def parent_instance(self):
        """Return the instance of the inline parent model."""
        return getattr(self, self._meta.crf_inline_parent)

    @property
    def parent_model(self) -> TSubjectVisitModelStub:
        """Return the class of the inline parent model."""
        field = getattr(self.__class__, self._meta.crf_inline_parent).field
        try:
            return field.rel.to
        except AttributeError:
            return field.remote_field.model  # django 2.0 +

    @property
    def subject_visit(self) -> SubjectVisitModelStub:
        """Return the instance of the inline parent model's visit
        model.
        """
        return getattr(self.parent_instance, self.visit_model_attr())

    def visit_model_attr(self):
        return self.parent_model.visit_model_attr()

    @property
    def report_datetime(self) -> datetime:
        """Return the instance of the inline parent model's
        report_datetime.
        """
        return self.subject_visit.report_datetime

    class Meta:
        crf_inline_parent: str = None
        abstract = True
