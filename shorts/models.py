from django.db import models

from short_url.utils import generate_short_url


class ShortURL(models.Model):
    url = models.URLField(unique=True)
    short = models.URLField(unique=True, blank=True)
    created = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    visited = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.url

    def save(self, *args, **kwargs):
        if self.short is None or self.short == '':
            self.short = generate_short_url(self)
        super(ShortURL, self).save(*args, **kwargs)
