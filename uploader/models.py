from os.path import basename
from django.db import models

# Create your models here.
class UploadedFile(models.Model):
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='uploads/%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    def __str__(self):
        return self.title or basename(self.file.name)

    class Meta:
        ordering = ['-uploaded_at']