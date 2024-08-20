from django import forms
from .models import gym_members,gym_item,gym_trainor
from django.core.exceptions import ValidationError

class RegisterFormMember(forms.ModelForm):
    expiry = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d'],
        label="Expiry Date"
    )

    class Meta:
        model = gym_members
        fields = ['id_card', 'expiry', 'membership', 'first_name', 'last_name', 'phone_number', 'address']
        
    def clean_id_card(self):
        id_card = self.cleaned_data.get('id_card')
        if gym_members.objects.filter(id_card=id_card).exists():
            raise ValidationError(f'This ID {id_card} card already exists')
        return id_card
    
    
    
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