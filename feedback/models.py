import datetime

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError


def validate_first(value): 
    if "cat" in value: 
        return value
    else: 
        raise ValidationError("Read the prompt again.") 

def validate_third(value): 
    if "love" in value: 
        return value
    else: 
        raise ValidationError("Read the prompt again.") 

def validate_fourth(value): 
    if "because" in value: 
        return value 
    else: 
        raise ValidationError("Read the prompt again.") 
        

class Feedback(models.Model):
    field1 = models.CharField(max_length = 200, validators =[validate_first] )
    field2 = models.PositiveSmallIntegerField(validators=[MinValueValidator(501), MaxValueValidator(1340)])
    field3 = models.CharField(max_length = 200, validators =[validate_third] )
    field4 = models.CharField(max_length = 200, validators =[validate_fourth]  )
    name = models.CharField(max_length = 200)
    def __str__(self):
        return self.name