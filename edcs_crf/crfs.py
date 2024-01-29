from edcs_subject.forms_collection import FormsCollection

from .crf import Crf

enrollment_crf = FormsCollection(
    Crf(show_order=100, model="edcs_subject.enrollmentcrf"),
    Crf(show_order=110, model="edcs_subject.respiratorysample"),
    Crf(show_order=115, model="edcs_subject.diagnostictests"),
    Crf(show_order=116, model="edcs_subject.drugsusceptibilitytests"),
    Crf(show_order=117, model="edcs_subject.diagnosiscrf"),
    name="Enrollment CRFs",
)

followup_crf = FormsCollection(
    Crf(show_order=100, model="edcs_subject.enrollmentcrf"),
    name="Follow Up CRFs",
)
