from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, MultiField, HTML, Div, Submit, Button
from crispy_forms.bootstrap import FormActions,InlineField
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class SignUpSmall(UserCreationForm):
	username = forms.CharField(
		label='',
		max_length=100,
		widget=forms.TextInput(attrs={'placeholder': 'Username','name':'user'}),
	)
	email = forms.EmailField(
		label='',
		max_length=100,
		widget=forms.TextInput(attrs={'placeholder': 'Email','name':'email'}),
	)
	password1 = forms.CharField(
		label='',
		max_length=100,
		widget=forms.TextInput(attrs={'placeholder': 'Password','name':'password1'}),
	)
	password2 = forms.CharField(
		label='',
		max_length=100,
		widget=forms.TextInput(attrs={'placeholder': 'Confirm Password','name':'password2'}),
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
				'username',
				'email',
				'password1',
				'password2',
				'terms_cond',
			),
			FormActions(
 	   			Submit('save', 'Register'),
    			Button('cancel', 'Already have an account?')
			),
		)
		
		class Meta:
			model = User
    		fields = ('username', 'email', 'password1', 'password2')

		
		
		
class SignIn(forms.Form):
	username = forms.CharField(
		label='',
		max_length=100,
		widget=forms.TextInput(attrs={'placeholder': 'Username','name':'user'}),
	)
	password = forms.CharField(
		label='',
		max_length=100,
		widget=forms.TextInput(attrs={'placeholder': 'Password','name':'password'}),
	)
		
	def __init__(self,*args,**kwargs):
		super(SignIn,self).__init__(*args,**kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'POST'
		self.helper.form_class = 'form-horizontal'
		self.helper.form_id = 'loginForm'
		self.helper.label_class='col-lg-2'
		self.helper.field_class='col-lg-8 col-md-offset-2'
		self.helper.layout = Layout(
			Fieldset(		
				'',
				'username',
				'password',
			),
			FormActions(
 	   			Submit('save', 'Sign in'),
    			Button('cancel', 'Dont have an account? Sign Up')
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

