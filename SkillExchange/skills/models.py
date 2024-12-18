from django.db import models

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=255)  
    image = models.ImageField(upload_to='images/skills/', blank=True, null=True)
    description = models.TextField(max_length=600)

    def __str__(self):
        return self.name