from django import forms
from .models import SummerNote
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
          model = Post
          fields = ('situation', 'country', 'material')
      #     fields = ('title', 'content', 'situation', 'country', 'material')
      #   fields = ('title', 'content', 'situation', 'country', 'material', 'photo')

#     def __init__(self, *args, **kwargs):
#         super(PostForm, self).__init__(*args, **kwargs)
#         self.fields['photo'].required = False #유효성 검사 패스

from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote import fields as summer_fields

class FormFromSomeModel(forms.ModelForm):

     fields = summer_fields.SummernoteTextFormField(error_messages={'required':(u'데이터를 입력해주세요'),})
     class Meta:
           model = SummerNote
           fields = ('fields',)

