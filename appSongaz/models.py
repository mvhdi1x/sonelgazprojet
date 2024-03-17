from django.contrib.auth.models import User
from django.db import models
import os


class File(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/')
    uploaded_at = models.DateTimeField(auto_now=True)
    # Link the file with the user
    user = models.ForeignKey(User, related_name="files", on_delete=models.CASCADE)

    def __str__(self):
        return os.path.basename(self.file.name)

    def filename(self):
        return os.path.basename(self.file.name)
