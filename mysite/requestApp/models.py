from datetime import datetime

from django.conf import settings
from django.contrib.auth.models import User, AbstractUser
from django.core.exceptions import ValidationError
from django.db import models

from userprofile.models import UserProfile


def get_default_pay_date():
    return datetime.today()


def validate_pay_date(value):
    if value < datetime.today().date():
        raise ValidationError(f'дата оплати не може бути меншою ніж дата заявки')


class Req(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, default=None,
                             verbose_name='Автор', related_name='reqs')
    req_date = models.DateTimeField(auto_now=True,
                                    verbose_name='Дата заявки')
    pay_date = models.DateField(verbose_name='Дата потреби',
                                default=get_default_pay_date,
                                help_text='<sup>план</sup>', )
    # validators=[validate_pay_date])
    target = models.TextField(max_length=500, verbose_name='Ціль',
                              error_messages={'blank': 'Необхідно заповнити це поле'})
    sum = models.IntegerField(default=0, verbose_name='Сума')

    receiver = models.CharField(max_length=50, verbose_name='Отримувач')
    is_ready = models.BooleanField(default=False, verbose_name='Готово для підпису')
    is_agreed = models.BooleanField(default=False, verbose_name='Узгоджено')
    photo_doc = models.ImageField(upload_to='images/users', verbose_name='фото документів', blank=True)

    info_text = models.CharField(max_length=500, blank=True, verbose_name='Дод інфо')

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'ЗаявкиРДС'
        ordering = ['-req_date']

    def __str__(self):
        return str(self.id) + ':  ' + f"{self.req_date:%d.%m.%Y}" + ': ' + str(self.sum) + ': ' + str(self.target)


class Agreed(models.Model):
    req = models.OneToOneField(Req, on_delete=models.CASCADE, unique=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True, default=None,
                             verbose_name='Узгодив')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата узгодження')

    class Meta:
        verbose_name = 'Узгодження'
        verbose_name_plural = 'Узгодження'
        ordering = ['-date']


class Message(models.Model):
    req = models.ForeignKey(Req, on_delete=models.CASCADE, related_name='messages')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, blank=True, null=True, default=None,
                             verbose_name='Автор повідомлення', related_name='messages')
    message_text = models.TextField(max_length=500, verbose_name='Повідомлення', blank=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата повідомлення')

    class Meta:
        verbose_name = 'Повідомлення'
        verbose_name_plural = 'Повідомлення'
        ordering = ['-date']

    def __str__(self):
        return str(self.id) + ':  ' + self.message_text[:10] + ': ' + str(self.req)
