from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from accounts.models import UserProfile
from django.forms import ModelForm
from grumblr_private.models import Post, Comment



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(required=True, help_text='Required.')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2','email' )


class EditUserProfileForm(forms.ModelForm):
	bio = forms.CharField(max_length=100, required=False)

	class Meta:
	    model = UserProfile
	    fields = ('age', 'bio', 'image')

	def __init__(self, *args, **kwargs):
		super(EditUserProfileForm, self).__init__(*args, **kwargs)
		f = self.fields.get('user_permissions', None)
		if f is not None:
		  f.queryset = f.queryset.select_related('content_type')

class EditUserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')

	def __init__(self, *args, **kwargs):
		super(EditUserForm, self).__init__(*args, **kwargs)
		f = self.fields.get('user_permissions', None)
		if f is not None:
		    f.queryset = f.queryset.select_related('content_type')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)