from django.forms import ModelForm, Textarea, CheckboxInput

from requestApp.models import Req, Agreed
from django.http import request


class ReqUpdateForm(ModelForm):
    class Meta:
        model = Req
        fields = ['pay_date', 'target', 'sum', 'receiver', 'is_ready', 'photo_doc', 'info_text']

        fields += ['is_agreed', ]

        widgets = {
            'target': Textarea(attrs={'cols': 29, 'rows': 3}),
            'is_agreed': CheckboxInput(attrs={'disabled': True}),
        }


class ReqAgreeForm(ModelForm):
    class Meta:
        model = Agreed
        fields = '__all__'




