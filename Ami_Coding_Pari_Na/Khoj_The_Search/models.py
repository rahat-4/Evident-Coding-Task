from django.db import models
from django.conf import settings
from django.core.validators import validate_comma_separated_integer_list

# Create your models here.
class ValueList(models.Model):
    #set one to many relationships with MyUser model
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name='payload')
    input_values = models.CharField(validators=[validate_comma_separated_integer_list], max_length=2048, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.email