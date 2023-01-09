import datetime

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


def get_default_pay_date():
    return timezone.now() + datetime.timedelta(days=3)


# def get_default_req_code():
#     yymmddhhmmss = (timezone.now())
#     a = yymmddhhmmss.strftime("%y %m %d %H:%M:%S")
#
#     return 'Thor_' + str(a)


class Req(models.Model):
    req_code = models.CharField(max_length=23, default=None)
    user = models.ForeignKey(User, on_delete=models.PROTECT, default=None,
                             verbose_name='Автор', related_name='reqs')
    req_date = models.DateTimeField(auto_now=True,
                                    verbose_name='Дата заявки')
    pay_date = models.DateField(verbose_name='Дата потреби',
                                default=get_default_pay_date(),
                                help_text='<sup>план</sup>', )

    target = models.TextField(max_length=500, verbose_name='Ціль')

    sum = models.IntegerField( verbose_name='Сума')
    receiver = models.CharField(max_length=50, verbose_name='Отримувач')
    doc = models.ImageField(upload_to='images/', blank=True)
    is_ready = models.BooleanField(default=False, verbose_name='Підписати')
    is_agreed = models.BooleanField(default=False, verbose_name='Узгоджено')
    info_text = models.CharField(max_length=500, blank=True, verbose_name='Дод інфо')

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'ЗаявкиРДС'
        ordering = ['-req_date']

    def __str__(self):
        return str(self.id) + ':  ' + f"{self.req_date:%d.%m.%Y}" + ': ' + str(self.sum) + ': ' + str(self.target)


class Agreed(models.Model):
    req = models.ForeignKey(Req, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True, default=None, verbose_name='Узгодив')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата узгодження')

    class Meta:
        verbose_name = 'Узгодження'
        verbose_name_plural = 'Узгодження'
        ordering = ['-date']
        unique_together = ('req', 'user')

    def __str__(self):
        return str(self.user) + ':  ' + str(self.req)[:10]

class Message(models.Model):
    req = models.ForeignKey(Req, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, blank=True, null=True, default=None,
                             verbose_name='Автор повідомлення', related_name='messages')
    message_text = models.TextField(max_length=500, verbose_name='Повідомлення', blank=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата повідомлення')

    class Meta:
        verbose_name = 'Повідомлення'
        verbose_name_plural = 'Повідомлення'
        ordering = ['date']

    def __str__(self):
        return str(self.id) + ':  ' + self.message_text[:10] + ': ' + str(self.req)
