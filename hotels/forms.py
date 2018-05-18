from django.forms import ModelForm
from .models import Hotel


class HotelForm(ModelForm):
    class Meta:
        model = Hotel
        fields = ['location', 'standard']

    def __init__(self, *args, **kwargs):
        super(HotelForm, self).__init__(*args, **kwargs)
        self.fields['location'].required = False
        self.fields['standard'].required = False