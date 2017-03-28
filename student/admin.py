from django.contrib import admin

from student.models import StudentData, BranchData, SemesterData


class StudentDataAdmin(admin.ModelAdmin):
    list_display = []


admin.site.register(StudentData, StudentDataAdmin)


class BranchDataAdmin(admin.ModelAdmin):
    list_display = []


admin.site.register(BranchData, BranchDataAdmin)


class SemesterDataAdmin(admin.ModelAdmin):
    list_display = []


admin.site.register(SemesterData, SemesterDataAdmin)
