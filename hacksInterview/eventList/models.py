from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='project_image', default='default.jpg')

    # TODO: Add field for description and migrate it (Textfield)

    # TODO: If they can, implement __str__ function for admin site display