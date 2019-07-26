from django import forms
from .models import Store, MachineID

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ('photo', 'store_name', 'menu', 'tel', 'time', 'day', 'park', 'address', 'tag')

#     def __init__(self, *args, **kwargs):
# #         super(PostForm, self).__init__(*args, **kwargs)
# #         self.fields['photo'].required = False #유효성 검사 패스