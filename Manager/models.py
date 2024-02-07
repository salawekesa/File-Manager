from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from cryptography.fernet import Fernet
from django.conf import settings
import base64, os
from django.dispatch import receiver


# Create your models here.


CLASSIFICATION_CHOICES = [
    ('Unclassified', 'Unclassified'),
    ('Confidential', 'Confidential'),
    ('Secret', 'Secret'),
    ('Top Secret', 'Top Secret'),
]

PRIORITIZATION_CHOICES = [
    ('Low', 'Low'),
    ('Medium', 'Medium'),
    ('High', 'High'),
]

FOLDER_CHOICES = [
    ('Group A', 'Group A'),
    ('Group B', 'Group B'),
    ('Group C', 'Group C'),
]

# class Folder(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name


class IncomingFiles(models.Model):
    sender = models.CharField(max_length=100)
    recipient = models.CharField(max_length=100)
    subject = models.CharField(max_length=255)
    date_sent = models.DateField()
    date_received = models.DateField()
    addressed_to = models.CharField(max_length=100)
    signatory = models.CharField(max_length=100)
    document = models.FileField(upload_to='incoming_files/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    prioritization = models.CharField(max_length=20, choices=PRIORITIZATION_CHOICES, default=[], blank=False)
    classification = models.CharField(max_length=20, choices=CLASSIFICATION_CHOICES, default=[], blank=False)
    folder = models.CharField(max_length=20, choices=FOLDER_CHOICES, default=[], blank=False)

    class Meta:
        ordering = ['-created_at', '-folder', 'subject']

    def __str__(self):
        return f"{self.sender} - {self.subject} - {self.addressed_to}"

def get_share_url(self):
        fernet = Fernet(settings.ID_ENCRYPTION_KEY)
        value = fernet.encrypt(str(self.pk).encode())
        value = base64.urlsafe_b64encode(value).decode()
        return reverse("share-file-id", kwargs={"id": (value)})

@receiver(models.signals.post_delete, sender=IncomingFiles)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.file_path:
        if os.path.isfile(instance.file_path.path):
            os.remove(instance.file_path.path)

@receiver(models.signals.pre_save, sender=IncomingFiles)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).file_path
    except sender.DoesNotExist:
        return False

    new_file = instance.file_path
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)