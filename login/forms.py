from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
  email = forms.EmailField()

  class Meta:
    model = User
    fields = ["username", "email", "password1", "password2"]

class CommentForm(forms.Form):
  secure_comment = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control rounded-5 p-2 mb-4'}), label="Enter safe comment here:", initial="<script>alert('This is a safe comment, since it uses Django.');</script>")
  unsecure_comment = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control rounded-5 p-2 mb-4'}), label="Enter malicious text that will be displayed in an alert:", initial='<script>alert("This is a malicious script!");</script>')