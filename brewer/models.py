
from django.contrib.auth.models import User
from django.db import models

import brewer as brewer_constants


class Course(models.Model):
    name = models.CharField(
        max_length=150,
        default='',
        blank=False,
    )
    professor_firstname = models.CharField(
        max_length=50,
        default='',
        blank=True,
    )
    professor_lastname = models.CharField(
        max_length=50,
        default='',
        blank=True,
    )
    manager = models.ForeignKey(User, related_name='manager+')
    students = models.ManyToManyField(User, related_name='students+', through='Membership')

    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'Courses'


class CourseSchedule(models.Model):
    course = models.ForeignKey(Course)
    start_time = models.TimeField()
    end_time = models.TimeField()
    weekday = models.PositiveSmallIntegerField()

    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.course.name

    class Meta:
        db_table = 'CourseSchedules'


class Membership(models.Model):

    member = models.ForeignKey(User)
    course = models.ForeignKey(Course)
    status = models.PositiveSmallIntegerField()

    def __unicode__(self):
        return self.id

    class Meta:
        db_table = 'Memberships'


class Topic(models.Model):
    title = models.CharField(
        max_length=150,
        default='',
        blank=False,
    )
    content = models.CharField(
        max_length=500,
        default='',
        blank=False,
    )
    author = models.ForeignKey(User)
    course = models.ForeignKey(Course)
    status = models.PositiveSmallIntegerField(default=1)

    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.id

    class Meta:
        db_table = 'Topics'


class Post(models.Model):
    content = models.CharField(
        max_length=500,
        default='',
        blank=False,
    )
    author = models.ForeignKey(User)
    topic = models.ForeignKey(Topic)

    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.id

    class Meta:
        db_table = 'Posts'
