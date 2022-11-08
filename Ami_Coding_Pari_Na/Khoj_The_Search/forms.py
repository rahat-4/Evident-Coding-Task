from django import forms

from .models import ValueList

#create value list form
class ValueListForm(forms.ModelForm):
    #modifying form fields
    value_list = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={"placeholder":"Input Here"}))
    search_here = forms.IntegerField(label="", required=False, widget=forms.TextInput(attrs={"placeholder":"Search Here"}))
    
    class Meta:
        model = ValueList
        fields = ['value_list', 'search_here']