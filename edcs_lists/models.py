from edcs_list_data.model_mixins import ListModelMixin


class InfoTbDxMade(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Info TB Diagnosis made"
        verbose_name_plural = "Info TB Diagnosis made"


class OtherDxMade(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Other Diagnosis made"
        verbose_name_plural = "Other Diagnosis made"
