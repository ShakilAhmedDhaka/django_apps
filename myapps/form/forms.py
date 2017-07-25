from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit


class SignUpSmall(forms.Form):
	first_name = forms.CharField(
		label='First Name',
		max_length=100,
	)
	last_name = forms.CharField(
		label='Last Name',
		max_length=100,
	)
	user_id = forms.CharField(
		label='User ID',
		max_length=100,
	)
	email_id = forms.EmailField(
		label='Email',
		max_length=100,
	)
	passwd = forms.CharField(
		label='Password',
		max_length=100,
	)
	conf_passwd = forms.CharField(
		label='Confirm Password',
		max_length=100,
	)
	
	def __init__(self,*args,**kwargs):
		super(SignUpSmall,self).__init__(*args,**kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'POST'
		self.helper.form_class = 'form-horizontal'
		#self.helper.add_input(Submit('signup_small','Sign Up',css_class='brn-primary'))	
	

		self.helper.label_class='col-lg-2'
		self.helper.field_class='col-lg-8'	
		#self.helper.form_tag = False
	



class ExampleForm(forms.Form):
	like_website = forms.TypedChoiceField(
		label = "Do you like this website?",
		choices = ((1,"Yes"),(0,"No")),
		coerce = lambda x: bool(int(x)),
		widget = forms.RadioSelect,
		initial = '1',
		required = True,
	)

	favorite_food = forms.CharField(
		label = "What is your favorite food?",
		max_length = 80,
		required = True,
	)
	
	favorite_color = forms.CharField(
		label = "What is your favorite color?",
		max_length = 80,
		required = True,
	)

	favorite_number = forms.CharField(
		label = "What is your favorite number?",
		max_length = 80,
		required = True,
	)

	notes = forms.CharField(
		label = "Additional notes or feedback",
		required = True,
	)
	

	def __init__(self,*args,**kwargs):
		super(ExampleForm,self).__init__(*args,**kwargs)
		self.helper=FormHelper()
		self.helper.form_id = 'id-exampleForm'
		#self.helper.form_class='blueForms'
		self.helper.label_class= 'col-lg-2'
		self.helper.field_class= 'col-lg-8'
		#self.helper.form_method='POST'
		#self.helper.form_action='submit_survey'
		#self.helper.form_tag = False	
		
		#self.helper.add_input(Submit('submit','Submit'))


class ButtonForm(forms.Form):
	

	def __init__(self,*args,**kwargs):
		super(ButtonForm,self).__init__(*args,**kwargs)
		self.helper = FormHelper()
		self.helper.form_id = 'id-buttonform'
		self.helper.label_class='col-lg-2'
		self.helper.field_class='col-lg-8'
		self.helper.add_input(Submit('submit','Submit'))
		


