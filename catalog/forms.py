from django import forms
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from django.forms import ModelForm
from catalog.models import BookInstance

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks(default=3)")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        #Check if a dateis not in the past
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        #Check if date is after 4 weeks
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal date more than 4 weeks'))

        return data

class RenewBookModelForm(ModelForm):
    class Meta:
        model = BookInstance
        fields = ['due_back']
        labels = {'due_back': _('New Renewal date')}
        help_texts = {'due_back': _('Enter a date between now and 4 weeks (default : 3).')}
        