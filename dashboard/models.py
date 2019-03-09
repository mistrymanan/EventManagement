from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    image = models.ImageField(blank=True, upload_to='EventImages',default='')

    def __str__(self):
        return self.name
