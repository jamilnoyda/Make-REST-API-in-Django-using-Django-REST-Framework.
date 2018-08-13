from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from models import Profile


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(
        max_length=254, help_text='Required. Provide a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2', )


class ProfileForm(forms.Form):
    enroll_number = forms.IntegerField(
        required=True, help_text='Required !!')

    STUDENT = 'Student'
    TEACHER = 'Teacher'
    ROLE_CHOICES = (
        (STUDENT, 'Student'),
        (TEACHER, 'Teacher'),
    )

    def save(self, user_name):
        data = self.cleaned_data
        user = get_object_or_404(User, username=user_name)
        userProfile = Profile(user=user, enroll_number=data[
                              'enroll_number'], role='Student',)
        userProfile.save()
