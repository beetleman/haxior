from django.db import models

# Create your models here.


class Dane(models.Model):
    POST = 'p'
    GET = 'g'
    TYPE_CHOICES = (
        (POST, 'POST'),
        (GET, 'GET'),
    )
    url = models.CharField('ukradziony url', max_length=300)
    type = models.CharField(
        'Type zapytania HTTP',
        max_length=1,
        choices=TYPE_CHOICES,
        default=POST
    )
    data = models.TextField('Tresc zapytania')

    class Meta:
        verbose_name = 'Skradzione dane'
        verbose_name_plural = 'Skradzione dane'

    def __unicode__(self):
        return self.url
