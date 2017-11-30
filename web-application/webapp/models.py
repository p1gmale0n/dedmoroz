from django.db import models
from django.utils.translation import ugettext_lazy as _

ACTIVE = 'AC'
MODERATION = 'MD'
DECLINE = 'DC'

STATUS_CHOICES = (
    (ACTIVE, _('Свободен')),
    (MODERATION, _('На расмотрение')),
    (DECLINE, _('Забронирован')),
)


class Organization(models.Model):
    name = models.CharField(max_length=150, verbose_name=_('Название организации'))
    street_address = models.CharField(max_length=350, verbose_name=_('Адрес организации'))
    phone = models.CharField(max_length=180, verbose_name=_('Номер телеофна организации'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Организация")
        verbose_name_plural = _("Организации")


class Letter(models.Model):
    image = models.ImageField(verbose_name=_("Письмо"), upload_to='images')
    status = models.CharField(choices=STATUS_CHOICES, max_length=2, default='AC', verbose_name=_('Статус'))
    organization = models.ForeignKey(Organization, related_name='letters', blank=True, null=True)

    class Meta:
        verbose_name = _("Письмо")
        verbose_name_plural = _("Письма")
