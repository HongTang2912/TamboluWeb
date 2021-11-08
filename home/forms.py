from django.forms import ModelForm
from .models import Cart

#def CartForm(forms.Form):
class CartForm(ModelForm):
    class Meta:
        model = Cart
        exclude = ('id',)

