from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Book(models.Model):
    storage = models.CharField(max_length=128, blank=True)
    fond  = models.CharField(max_length=128, default=None, null=True, blank=True)
    inventory  = models.CharField(max_length=128, default=None, null=True, blank=True)
    number  = models.CharField(max_length=128, default=None, null=True, blank=True)
    exodus  = models.CharField(max_length=128, default=None, null=True, blank=True)
    months= ArrayField(models.CharField(max_length=64), blank=True, null=True, default=None)
    months_numbers = ArrayField(models.IntegerField(), blank=True, default=None, null=True)
    special_name = models.CharField(max_length=512, default=None, null=True)
    dating  = models.CharField(max_length=128, default=None, null=True, blank=True)
    size = models.IntegerField(null=True, default=None)
    book_format = models.CharField(max_length=128, default=None, null=True, blank=True)
    book_type = models.CharField(max_length=128, default=None, null=True, blank=True)
    file_path = models.CharField(max_length=512, default=None, null=True, blank=True)
    handwriting = models.CharField(max_length=128, default=None, null=True, blank=True)
    material = models.CharField(max_length=128, default=None, null=True, blank=True)
    description = models.CharField(max_length=512, default=None, null=True, blank=True)
    additional_info = models.TextField(default=None, null=True, blank=True)