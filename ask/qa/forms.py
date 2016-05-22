from django import forms
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.forms import ModelForm
from .models import Question, Answer
from datetime import datetime
from django.contrib.auth import authenticate, login

"""
class AskForm(ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
"""

class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)
   
    def clean_title(self):
        title = self.cleaned_data['title']
        if title.strip() == '':
            raise forms.ValidationError('Title is empty', 
                                        code='validation_error')
        return title

    def clean_text(self):
        text = self.cleaned_data['text']
        if text.strip() == '':
            raise forms.ValidationError('Text is empty',
                                        code='validation_error')
        return text
            
    def save(self):
        if self._user.is_anonymous():
            self.cleaned_data['author_id'] = 1
        else:
            self.cleaned_data['author'] = self._user
        question = Question(**self.cleaned_data)
        question.save()
        return question

"""
class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = '__all__'
"""


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)

    def clean_text(self):
        text = self.cleaned_data['text']
        if text.strip() == '': 
            raise forms.ValidationError('Text is empty',
                                        code='validation_error')
        return text

    def clean_question(self):
        try:
            question = int(self.cleaned_data['question'])
        except ValueError:
            raise forms.ValidationError('Invalid data',
                                        code='validation_error')
        return question

    
    def save(self):
        self.cleaned_data['question'] = get_object_or_404(
            Question,
            pk=self.cleaned_data['question'])
        if self._user.is_anonymous():
            self.cleaned_data['author_id'] = 1
        else:
            self.cleaned_data['author'] = self._user
	answer = Answer(**self.cleaned_data)
        answer.save()
	return answer

"""
class SignupForm(ModelForm):
    # https://docs.djangoproject.com/en/1.8/_modules/django/contrib/auth/forms/#UserCreationForm
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
"""

class SignupForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if username.strip() == '':
            raise forms.ValidationError('Username is empty',
                                        code='validation_error')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if email.strip() == '':
            raise forms.ValidationError('Email is empty',
                                        code='validation_error')
        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        if password.strip() == '':
            raise forms.ValidationError('Password is empty',
                                        code='validation_error')
        return password

    def save(self):
        user = User.objects.create_user(**self.cleaned_data)
        user.save()
        auth = authenticate(**self.cleaned_data)
        return auth

"""
class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
"""


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if username.strip() == '':
            raise forms.ValidationError('Username is empty',
                                        code='validation_error')
        return username

    def clean_password(self):
        password = self.cleaned_data['password']
        if password.strip() == '':
            raise forms.ValidationError('Password is empty',
                                        code='validation_error')
        return password

    def save(self):
        auth = authenticate(**self.cleaned_data)
        return auth
