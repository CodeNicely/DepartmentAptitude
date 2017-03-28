from __future__ import unicode_literals

from django.db import models


class SemesterData(models.Model):
    semester_name = models.CharField(max_length=256)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.semester_name


class BranchData(models.Model):
    branch_name = models.CharField(max_length=256)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.branch_name


# Create your models here.

class StudentData(models.Model):
    enrollment_number = models.IntegerField()
    roll_number = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    mobile = models.IntegerField()
    email = models.CharField(max_length=256, null=False, blank=False)
    password = models.CharField(max_length=256, null=False, blank=False)
    semester = models.ForeignKey(SemesterData)
    branch = models.ForeignKey(BranchData)
    mobile_verified = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
