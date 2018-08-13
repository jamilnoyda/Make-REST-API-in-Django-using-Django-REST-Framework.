from django import forms
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import IntegrityError
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from accounts.models import Profile
from django.forms import ModelForm

from result.models import Standard, Marksheet


class StandardForm(ModelForm):

    class Meta:
        model = Standard
        fields = '__all__'


class SendPDFForm(forms.Form):
    select_standard = forms.ModelChoiceField(
        queryset=Standard.objects.all())
    enroll_number = forms.CharField(
        required=True,
        label='Enrollment Number',
        max_length=32
    )
    pdf_file = forms.FileField(
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    class Meta:
        model = Marksheet
        fields = ['pdf_file']

    def save(self, request):
        from result.models import Marksheet
        data = self.cleaned_data
        try:
            student_obj = Profile.objects.filter(
                user__is_active=True, enroll_number=data['enroll_number']).first()
            marksheet = Marksheet(standard=data[
                                  'select_standard'], student_name=student_obj, pdf_file=data['pdf_file'])
            marksheet.save()
            messages.success(request, 'Marksheet for Enrollment Number {enroll_number} has been uploaded and mail has been sent successfully.'.format(
                enroll_number=data['enroll_number']))
        except IntegrityError:
            messages.success(request, 'Enter Valid Enroll Number')
            return redirect('/teachers/')
        except:
            messages.success(
                request, 'Something went wrong! Please, try again')
            return redirect('/teachers/')


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2', )


class ProfileForm(forms.Form):
    STUDENT = 'Student'
    TEACHER = 'Teacher'
    ROLE_CHOICES = (
        (STUDENT, 'Student'),
        (TEACHER, 'Teacher'),
    )

    def save(self, user_name):
        user = get_object_or_404(User, username=user_name)
        user.is_staff = True
        user.save()
        userProfile = Profile(user=user, role='Teacher',)
        userProfile.save()
