from django import forms
from .models import House, HousePrice

class HouseForm(forms.ModelForm):

    asking_price = forms.IntegerField()


    class Meta:
        model = House
        fields = '__all__'
