from django import forms
from django.forms import ModelForm
from posts.models import TextPost
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit



class TextPostForm(ModelForm):
	class Meta:
		model = TextPost
		fields = ['content']
		
	def __init__(self, *args, **kwargs):
		super(TextPostForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_id = 'text-post-form'
		self.helper.form_class = 'blueForms'
		self.helper.form_method = 'post'
		self.helper.form_action = 'posts:submit_post'

		self.helper.add_input(Submit('submit', 'Submit'))