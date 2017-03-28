from __future__ import unicode_literals

from django.db import models

from question.models import DifficultyData, SubjectData, QuestionData, OptionData
from student.models import StudentData


class QuizData(models.Model):
    quiz_name = models.CharField(max_length=256)
    quiz_description = models.CharField(max_length=256)
    quiz_time = models.IntegerField()
    per_question_marks = models.IntegerField()
    difficulty_id = models.ForeignKey(DifficultyData)
    quiz_status = models.BooleanField()
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.id


class QuizSubjectData(models.Model):
    subject_id = models.ForeignKey(SubjectData)
    quiz_id = models.ForeignKey(QuizData)
    number_of_questions = models.IntegerField()
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)


class QuizQuestionData(models.Model):
    quiz_id = models.ForeignKey(QuizData)
    question_id = models.ForeignKey(QuestionData)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)


class QuizResponseData(models.Model):
    quiz_id = models.ForeignKey(QuizData)
    roll_number = models.ForeignKey(StudentData)
    marks = models.IntegerField()


class QuizQuestionResponseData(models.Model):
    quiz_id = models.ForeignKey(QuizData)
    question_id = models.ForeignKey(QuestionData)
    option_id = models.ForeignKey(OptionData)
    correct_flag = models.BooleanField(default=False)
