from __future__ import unicode_literals

from django.db import models


# Create your models here.

class DifficultyData(models.Model):
    difficulty_type = models.CharField(max_length=256)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.difficulty_type


class SubjectData(models.Model):
    subject_name = models.CharField(max_length=256)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.subject_name


class QuestionData(models.Model):
    question = models.CharField(max_length=2048)
    question_hint = models.CharField(max_length=2048)
    difficulty_level = models.ForeignKey(DifficultyData)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.question


class OptionData(models.Model):
    question_id = models.ForeignKey(QuestionData)
    option = models.CharField(max_length=256)
    correct_flag = models.BooleanField(default=False)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.option


class QuestionSubjectData(models.Model):
    question_id = models.ForeignKey(QuestionData)
    subject_id = models.ForeignKey(SubjectData)
