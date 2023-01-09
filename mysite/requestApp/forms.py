from django.forms import *

from requestApp.models import *


def form_fields():
    return ['pay_date',
            'target',
            'sum',
            'receiver',
            # 'doc',
            'is_ready',
            'info_text',
            ]


class ReqUpdateForm(ModelForm):
    class Meta:
        model = Req
        fields = form_fields()
        widgets = {
            'target': Textarea(attrs={'cols': 29, 'rows': 3}),
            'pay_date': DateInput(format='%d.%m.%Y'),

        }


class ReqCreateForm(ModelForm):
    class Meta:
        model = Req
        fields = form_fields()
        widgets = {
            'target': Textarea(attrs={'cols': 29, 'rows': 5}),
        }
        #TODO як змінити назву лейбла для поля віджета ?

class MessageCreateForm(ModelForm):
    class Meta:
        model = Message
        fields = ['message_text']
        widgets = {
            'message_text': Textarea(attrs={'cols': 25, 'rows': 3}),
        }


class MessageUpdateForm(ModelForm):
    class Meta:
        model = Message
        fields = ['message_text']
        widgets = {
            'message_text': Textarea(attrs={'cols': 58, 'rows': 1}),
        }
