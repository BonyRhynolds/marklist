from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class details(models.Model):
    Name=models.CharField(max_length=25)
    Mark1=models.IntegerField()
    mark2=models.IntegerField()

    def __str__(self):
        return self.Name

class data(models.Model):
    Name=models.CharField(max_length=25)
    RegNo=models.IntegerField()
    Mark1=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    Mark2=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    Mark3=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])

    def __str__(self):
        return self.Name
    
    def total(self):
        return self.Mark1+self.Mark2+self.Mark3 
