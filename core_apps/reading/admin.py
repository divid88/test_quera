from django.contrib import admin

from .models import Subject, SubSubject,Concept


class SubSubjectAdmin(admin.StackedInline):
    model = SubSubject

class ConceptAdmin(admin.StackedInline):
    model = Concept

class SubSubjectAdmin(admin.ModelAdmin):
    inlines = [ConceptAdmin]


admin.site.register(Subject)

admin.site.register(SubSubject, SubSubjectAdmin)