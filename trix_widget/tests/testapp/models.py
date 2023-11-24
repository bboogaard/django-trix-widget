from django.db import models

from trix_widget.fields import TrixField


class TrixModel(models.Model):

    text = TrixField()
