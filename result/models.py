# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.mail import EmailMessage
from django.core.validators import FileExtensionValidator
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import Profile

# Create your models here.


class Standard(models.Model):
    name = models.CharField(
        max_length=20, help_text='add Standard for ex. Standard 1')

    def __unicode__(self):
        return self.name


class Marksheet(models.Model):
    standard = models.ForeignKey(
        Standard, on_delete=models.CASCADE, help_text='Select Standard')
    uploaded_on = models.DateField(
        auto_now_add=True, help_text='File to Uploaded on')
    student_name = models.ForeignKey(
        Profile, related_name='marksheets', on_delete=models.CASCADE, help_text='Student Name')
    pdf_file = models.FileField(unique=True, upload_to='uploads/%Y/%m/%d/', default="Error to Showing file",
                                validators=[FileExtensionValidator(allowed_extensions=['pdf'])], help_text='Select file to upload.')

    class Meta:
        ordering = ['uploaded_on']

        def __unicode__(self):
            return self.student_name.user.username

    def __unicode__(self):
        return self.student_name.user.username

    def get_absolute_url(self):
        return reverse('students:marksheet-detail', kwargs={"pk": self.pk})


@receiver(post_save, sender=Marksheet)
def send_user_notification_callback(sender, **kwargs):
    """
    Callback for notifying student about marksheet.
    """
    instance = kwargs['instance']
    user = instance.student_name.user
    email = user.email
    pdf_url = instance.pdf_file.url

    html_content = "Welcome %s to Python School. Your Marksheet is available.\nYou can download it from your account or click the link below to dowload:\nhttp://localhost:8000{url}".format(
        url=pdf_url)

    message = EmailMessage(subject='welcome', body=html_content % (
        user), to=[email])
    message.content_subtype = 'html'
    message.send()
