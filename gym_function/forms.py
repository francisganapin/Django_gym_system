from django import forms
from .models import gym_members,gym_item,gym_trainor

class RegisterFormMember(forms.ModelForm):
    expiry = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d'],
        label="Expiry Date"
    )

    class Meta:
        model = gym_members
        fields = ['id_card', 'expiry', 'membership', 'first_name', 'last_name', 'phone_number', 'address']

class RegisterFormTrainor(forms.ModelForm):
      
      class Meta:
            model = gym_trainor
            fields = ['trainor_id', 'first_name', 'last_name', 'specialty', 'phone_number']
     
class UpdateFormMember(forms.ModelForm):
        expiry = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d'],
        label="Expiry Date"
    )
        class Meta:
            model = gym_members
            fields = ['id_card', 'expiry']

class DeleteFormMember(forms.ModelForm):
        expiry = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d'],
        label="Expiry Date"
    )
        class Meta:
            model = gym_members
            fields = ['id_card']\
            
class UpdateFormInvetory(forms.ModelForm):
        class Meta:
              model = gym_item
              fields = ['id','stock']