from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms

class CommentForm(forms.Form):
    comment=forms.CharField(required=True,widget=forms.Textarea)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'CommentFormId'
        self.helper.form_class = 'CommentForm'
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-2 mt-2'
        self.helper.field_class = 'col-8 mt-2'
        self.helper.layout = Layout(
               'comment',
               self.helper.add_input(Submit('submit', 'Submit'))
        )