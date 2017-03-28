from django.contrib import admin

from question.models import QuestionData, DifficultyData, SubjectData, QuestionSubjectData, OptionData


class QuestionDataAdmin(admin.ModelAdmin):
    list_display = ['question']


admin.site.register(QuestionData, QuestionDataAdmin)


class DifficultyDataAdmin(admin.ModelAdmin):
    list_display = []


admin.site.register(DifficultyData, DifficultyDataAdmin)


class SubjectDataAdmin(admin.ModelAdmin):
    list_display = []


admin.site.register(SubjectData, SubjectDataAdmin)


class QuestionSubjectDataAdmin(admin.ModelAdmin):
    list_display = []


admin.site.register(QuestionSubjectData, QuestionSubjectDataAdmin)


class OptionDataAdmin(admin.ModelAdmin):
    list_display = []


admin.site.register(OptionData, OptionDataAdmin)
