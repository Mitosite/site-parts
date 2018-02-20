import os

from django.db import models
from django.conf import settings


class File_upload(models.Model):
    file = models.FileField(upload_to= 'items')

    @property
    def relative_path(self):
        return os.path.relpath(self.path, settings.MEDIA_ROOT)


#how to download files stored in static if it seems they are in media root