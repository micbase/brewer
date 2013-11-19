
from django.contrib.auth.models import User
from django.db import models

#import brewer as brewer_constants


class Source(models.Model):
    variety = models.CharField(
        max_length=150,
        default='',
        blank=True,
    )
    name = models.CharField(
        max_length=150,
        default='',
        blank=False,
    )

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'Sources'


class Recipe(models.Model):
    brewer = models.ForeignKey(User)
    name = models.CharField(
        max_length=150,
        default='',
        blank=False,
    )
    inote = models.CharField(
        max_length=500,
        default='',
        blank=True,
    )
    note = models.CharField(
        max_length=500,
        default='',
        blank=True,
    )

    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'Recipes'


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe)
    source = models.ForeignKey(Source)
    amount = models.FloatField(blank=True)
    unit = models.CharField(
        max_length=20,
        default='',
        blank=True,
    )
    note = models.CharField(
        max_length=500,
        default='',
        blank=True,
    )
    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.recipe.name

    class Meta:
        db_table = 'Ingredients'


class Procedure(models.Model):

    recipe = models.ForeignKey(Recipe)

    title = models.CharField(
        max_length=100,
        default='',
        blank=True,
    )
    tag = models.CharField(
        max_length=100,
        default='',
        blank=True,
    )
    content = models.CharField(
        max_length=500,
        default='',
        blank=True,
    )
    note = models.CharField(
        max_length=500,
        default='',
        blank=True,
    )
    # order = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.id

    class Meta:
        db_table = 'Procedures'
