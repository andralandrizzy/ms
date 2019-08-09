from django import forms
from . models import Testimonial


class QuoteForm(forms.ModelForm):

    class Meta:
        model = Testimonial
        fields = ['quote', 'name', 'client_image']
