from django import forms
from .models import gym_members

class RegisterFormMember(forms.ModelForm):
    expiry = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d'],
        label="Expiry Date"
    )

    class Meta:
        model = gym_members
        fields = ['id_card', 'expiry', 'membership', 'first_name', 'last_name', 'phone_number', 'address']
