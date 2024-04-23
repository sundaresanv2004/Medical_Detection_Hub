from django.forms import ModelForm
from .models import UploadImage


class UploadImageForm(ModelForm):
    class Meta:
        model = UploadImage
        fields = ['image']

    def __init__(self, *args, **kwargs):
        super(UploadImageForm, self).__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'id': 'file-input'})
        self.fields['image'].label = False
        self.fields['image'].required = True
