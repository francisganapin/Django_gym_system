from django import forms
from .models import gym_members,gym_item,gym_trainor,gym_classes
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
        ''' This will check if id card is already exist 
        '''
        id_card = self.cleaned_data.get('id_card')
        if gym_members.objects.filter(id_card=id_card).exists():
            raise ValidationError(f'This ID {id_card} card already exists')
        return id_card
    
    
    
class RegisterFormTrainor(forms.ModelForm):
      
    class Meta:
            model = gym_trainor
            fields = ['trainor_id', 'first_name', 'last_name', 'specialty', 'phone_number']
     
    def clean_trainor_card(self):
        trainor_id = self.cleaned_data.get('trainor_id')
        if gym_trainor.objects.filter(trainor_id=trainor_id).exists():
              raise ValidationError(f'this ID Trainor {trainor_id} is already Exist')
        return trainor_id
        


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
            fields = ['id_card']
            
class InputFormInventory(forms.ModelForm):
    class Meta:
            model = gym_item
            fields = ['item_name','stock','description','supplier','phone_number']

    def clean_item_name(self):
        item_name = self.cleaned_data.get('item_name')
        if gym_item.objects.filter(item_name=item_name).exists():
            raise ValidationError(f'This item name "{item_name}" already exists.')
        return item_name



class UpdateFormInvetory(forms.ModelForm):
        class Meta:
              model = gym_item
              fields = ['id','stock']



class RegisterFormClases(forms.ModelForm):
      class Meta:
            model = gym_classes
            fields = ['class_name','class_type','class_day','class_hour','trainor_name']