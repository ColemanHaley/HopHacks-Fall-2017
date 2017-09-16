# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Course(models.Model):
    """
    Represents a course at a school, made unique by its course code.
    Courses persist across semesters and years. Their presence in a semester or year
    is indicated by the existence of sections assigned to that course for that semester
    or year. This is why a course does not have fields like professor, those varies.
    The course model maintains only attributes which tend not to vary across semesters
    or years.
    A course has many :obj:`Section` which a student can enroll in.
    Attributes:
        code (:obj:`CharField`): the course code without indication of section (E.g. EN.600.100)
        name (:obj:`CharField`): the general name of the course (E.g. Calculus I)
        description (:obj:`TextField`): the explanation of the content of the courzse
        department (:obj:`CharField`): department offering course (e.g. Computer Science)
        level (:obj:`CharField`): indicator of level of course (e.g. 100, 200, Upper, Lower, Grad)
        
    """
    code = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=250)
    description = models.TextField(default='')
    department = models.CharField(max_length=250, default='', null=True)
    level = models.CharField(max_length=500, default='', null=True)

    def __str__(self):
        return self.code + ": " + self.name