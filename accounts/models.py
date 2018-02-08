from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser


NORMAL = 'normal'
ADMIN = 'admin'
OBSERVER = 'observer'

TYPE_USER = (
    (NORMAL, _('Normal')),
    (ADMIN, _('Admin')),
    (OBSERVER, _('Observer'))
)


class Country(models.Model):
    name = models.CharField(_('Country name'), max_length=50, blank=False, null=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey('Country', related_name='Country_city', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(_('City name'), max_length=50, blank=False, null=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class User(AbstractUser):
    typeUser = models.CharField(_('Type User'), choices=TYPE_USER, max_length=10, default=NORMAL,
                                blank=False, null=False)
    image = models.ImageField(_('Profile photo'), max_length=255, blank=True, null=True)
    recovery = models.CharField(_('Recovery'), max_length=20, blank=True, null=True)
    dni = models.CharField(_('Dni'), max_length=20, blank=True, null=True)
    direction = models.CharField(_('Direction'), max_length=255, blank=True, null=True)
    phone = models.CharField(_('Phone'), max_length=20, blank=True, null=True)
    country = models.ForeignKey('Country', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.username

