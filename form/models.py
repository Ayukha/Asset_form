# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from .utils import RandomFileName

# Create your models here.

class Profile(models.Model):

    """Model representing a Form Fields"""

    name = models.CharField(max_length=100, db_index=True)
    adm_no = models.TextField(null=True, blank=True)
    email = models.TextField(null=True, blank=True)
    phno = models.TextField(null=True, blank=True)
    image = models.ImageField(
        upload_to=RandomFileName('images'),
        null=True, 
        blank=True, 
        verbose_name="Images")
    