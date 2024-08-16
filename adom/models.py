from django.db import models
from django.contrib.auth.models import User
import random
import string

class AudioRecording(models.Model):
    audio_data = models.TextField()  # Store the base64 encoded audio data
    username = models.CharField(max_length=150)  # Store the username
    uniq_id = models.CharField(max_length=5, unique=True, null=True, blank=True)  # New field
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Recording by {self.username} on {self.created_at}"

    def save(self, *args, **kwargs):
        if not self.uniq_id:
            self.uniq_id = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        super().save(*args, **kwargs)


from django.db import models
from django.contrib.auth.models import User

class AudioRecordo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_datetime = models.DateTimeField()
    # file_path = models.FilePathField()
    hymn_number = models.CharField(max_length=10)
    random_letters = models.CharField(max_length=10)


from django.db import models
from django.contrib.auth.models import User

class AudioRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_datetime = models.DateTimeField(auto_now_add=True)
    hymn_number = models.CharField(max_length=10)
    random_letters = models.CharField(max_length=10)
    tempo = models.FloatField(blank=True, null=True)  # New field

    def save(self, *args, **kwargs):
        # Delete any existing records with the same hymn_number and user
        AudioRecord.objects.filter(user=self.user, hymn_number=self.hymn_number).delete()

        # Call the original save method to save the new record
        super().save(*args, **kwargs)
