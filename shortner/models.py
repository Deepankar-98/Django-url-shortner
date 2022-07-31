from django.db import models

# Create your models here.
class URLShorten(models.Model):
    short = models.AutoField(unique=True, primary_key=True)
    url = models.URLField(blank=False, null=False, db_index=True)

    def __str__(self) :
        return str(self.url)