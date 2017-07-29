from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, MultiField, HTML, Div, Submit, Button
from crispy_forms.bootstrap import FormActions,InlineField
from django.core.exceptions import ValidationError



class SignUpSmall(forms.Form):
	user = forms.CharField(
		label='',
		max_length=100,
		widget=forms.TextInput(attrs={'placeholder': 'Username','name':'user'}),
	)
	email = forms.EmailField(
		label='',
		max_length=100,
		widget=forms.TextInput(attrs={'placeholder': 'Email','name':'email'}),
	)
	passwd = forms.CharField(
		label='',
		max_length=100,
		widget=forms.TextInput(attrs={'placeholder': 'Password','name':'passwd'}),
	)
	conf_passwd = forms.CharField(
		label='',
		max_length=100,
		widget=forms.TextInput(attrs={'placeholder': 'Confirm Password','name':'conf_passwd'}),
	)
	
	terms_cond = forms.BooleanField(
		label = 'I agree to terms and conditions',
	)
	

	def __init__(self,*args,**kwargs):
		super(SignUpSmall,self).__init__(*args,**kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'POST'
		self.helper.form_class = 'form-horizontal'
		self.helper.form_id = 'loginForm'
		#self.helper.attrs = {'data-toggle':'validator','role':'form'}
		

		self.helper.label_class='col-lg-2'
		self.helper.field_class='col-lg-8 col-md-offset-2'
		self.helper.layout = Layout(
			Fieldset(		
				'',
				'user',
				'email',
				'passwd',
				'conf_passwd',
				'terms_cond',
			),
			FormActions(
 	   			Submit('save', 'Register'),
    			Button('cancel', 'Already have an account?')
			),
		)
		

		
		



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
		self.helper.layout = Layout(
    			Fieldset(
        			'Tell us your favorite stuff',
            			'like_website',
            			'favorite_number',
				'favorite_color',
        			'favorite_food',
        			'notes'
    			)
		)
		

	


class ButtonForm(forms.Form):
	

	def __init__(self,*args,**kwargs):
		super(ButtonForm,self).__init__(*args,**kwargs)
		self.helper = FormHelper()
		self.helper.form_class = 'form-horizontal'
		self.helper.form_id = 'id-buttonform'
		self.helper.label_class='col-lg-2'
		self.helper.field_class='col-lg-8 col-md-offset-2'
		self.helper.layout = Layout(
			FormActions(
				Submit('{% url "signup_small" %}','Register'),
				Button('login','Already have an account?'),
			),
		)

