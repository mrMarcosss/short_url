from django import forms


class SubmitURLForm(forms.Form):
    url = forms.URLField()

    def __init__(self, *args, **kwargs):
        super(SubmitURLForm, self).__init__(*args, **kwargs)
        self.fields['url'].widget.attrs['class'] = 'form-control'
        self.fields['url'].widget.attrs['placeholder'] = 'Enter some url'
