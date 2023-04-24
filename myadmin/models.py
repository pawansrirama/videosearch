from django.db import models


# Create your models here.
class videoDetails(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/')
    thumbnail = models.FileField(upload_to='thumbnails/')
    uploaded_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

