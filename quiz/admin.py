from django.contrib import admin


# Register your models here.
from quiz.models import QuizData, QuizSubjectData, QuizQuestionData, QuizResponseData, QuizQuestionResponseData


class QuizDataAdmin(admin.ModelAdmin):
    list_display = []


admin.site.register(QuizData, QuizDataAdmin)


class QuizSubjectDataAdmin(admin.ModelAdmin):
    list_display = []


admin.site.register(QuizSubjectData, QuizSubjectDataAdmin)


class QuizQuestionDataAdmin(admin.ModelAdmin):
    list_display = []


admin.site.register(QuizQuestionData, QuizQuestionDataAdmin)


class QuizResponseDataAdmin(admin.ModelAdmin):
    list_display = []


admin.site.register(QuizResponseData, QuizResponseDataAdmin)


class QuizQuestionResponseDataAdmin(admin.ModelAdmin):
    list_display = []


admin.site.register(QuizQuestionResponseData, QuizQuestionResponseDataAdmin)
