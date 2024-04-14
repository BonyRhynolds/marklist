from django.db import models

# Create your models here.
class details(models.Model):
    Name=models.CharField(max_length=25)
    Mark1=models.IntegerField()
    mark2=models.IntegerField()

    def __str__(self):
        return self.Name
