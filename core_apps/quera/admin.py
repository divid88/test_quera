from django.contrib import admin

from .models import LevelUser, ProgramTest, SubjectTestProgram

admin.site.register(LevelUser)
admin.site.register(ProgramTest)

class SubProgramTest(admin.TabularInline):
    model = ProgramTest


class AdminSubjectTest(admin.ModelAdmin):
    inlines = [SubProgramTest]

admin.site.register(SubjectTestProgram, AdminSubjectTest)


