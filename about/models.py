from django.db import models
from cloudinary.models import CloudinaryField
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=200)
    profile_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title

class CollaborateRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField(
        validators=[
            MinLengthValidator(1, "The message must have at least 1 character."),
            MaxLengthValidator(2000, "The message cannot exceed 2000 characters.")
        ]
    )
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"
