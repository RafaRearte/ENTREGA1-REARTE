from django import forms
from django.forms import ModelForm
from app_rearte.models import House_pet, Money


class CarForm(forms.Form):
    brand = forms.CharField(max_length=40, min_length=3, label='Marca')
    model = forms.CharField(max_length=40, label='modelo')
    license_plate = forms.IntegerField(label='patente')
    year = forms.IntegerField(label='año')

#class CarForm(ModelForm):
#    class Meta:
#        model = Car
#        fields = '__all__'

class PersonForm(forms.Form):
    name = forms.CharField(max_length=40, label='Nombre')
    age = forms.IntegerField(label='Edad')
    birth_date = forms.DateField(
        label='Fecha de nacimiento',
        widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'})
    )
    occupation = forms.CharField(max_length=40, label='Ocupacion')

#class PersonForm(ModelForm):
#    class Meta:
#        model = Person
#        fields = '__all__'

class House_petForm(forms.Form):
    name = forms.CharField(max_length=40, label='Nombre')
    age = forms.IntegerField(label='Edad')
    birth_date = forms.DateField(
        label='Fecha de nacimiento',
        widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'})
    )
    animal = forms.CharField(max_length=40)
    breed = forms.CharField(max_length=40)

#class House_petForm(ModelForm):
#    class Meta:
#        model = House_pet
#        fields = '__all__'

class MoneyForm(forms.Form):
    type = forms.CharField(max_length=40)
    amount = forms.IntegerField()

#class MoneyForm(ModelForm):
#    class Meta:
#        model = Money
#        fields = '__all__'