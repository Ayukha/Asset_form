import os
import uuid
from django.conf import settings
from django.utils.deconstruct import deconstructible




@deconstructible
class RandomFileName(object):
    def __init__(self, path):
        self.path = path

    def __call__(self, instance, filename):
        extension = os.path.splitext(filename)[1]
        path = self.path
        if 'id' in self.path :
            path = self.path.format(id=instance.adm_no)
        filename = '{}{}'.format(instance.adm_no, extension)
        filename = os.path.join(path, filename)
        return filename