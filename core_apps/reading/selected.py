from .models import Subject, SubSubject, Concept


def get_subsubject(subject: int):

    query = SubSubject.objects.get(pk=subject).select_related('concepts').all()
    return query