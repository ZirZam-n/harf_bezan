from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class Post(models.Model):
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=100,
        null=False,
        blank=False,
    )

    author = models.CharField(
        verbose_name=_('Author'),
        max_length=100,
        null=False,
        blank=False,
    )

    text = models.TextField(
        null=False,
        blank=False,
        max_length=100000,
    )
