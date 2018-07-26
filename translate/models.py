from django.db import models
from django.contrib.auth.models import User


class TranslationEvent(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)
    # from_lang = models.ForeignKey(to=Language, on_delete=models.DO_NOTHING)
    # to_lang = models.ForeignKey(to=Language, on_delete=models.DO_NOTHING)
    from_lang = models.CharField(max_length=31)
    to_lang = models.CharField(max_length=31)
    text = models.TextField()
    translation = models.TextField()
    will_practice = models.BooleanField()
