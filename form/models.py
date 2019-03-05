# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from .util import RandomFileName

# Create your models here.

class Profile(models.Model):

    """Model representing a Form Fields"""

    name = models.CharField(max_length=50, db_index=True)
    adm_no = models.CharField(max_length=15,null=True, blank=True,unique=True)
    email = models.EmailField(max_length=30,null=True,blank=True)
    phno = models.IntegerField(null=True, blank=True)
    image1 = models.ImageField(null=True, blank=True, upload_to=RandomFileName("submission_files/submission_{id}"))
    image2 = models.ImageField(null=True, blank=True, upload_to=RandomFileName("submission_files/submission_{id}"))
    image3 = models.ImageField(null=True, blank=True, upload_to=RandomFileName("submission_files/submission_{id}"))

    def __str__(self):

        """Returns the title of Challenge"""
        return self.adm_no
