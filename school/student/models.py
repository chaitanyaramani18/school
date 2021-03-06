from django.db import models
from django.conf import settings

# Create your models here
class Student(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=120, null=False,blank=False)
    lastname = models.CharField(max_length = 120,null=False,blank=False)
    image = models.ImageField()
    studentid = models.IntegerField(null = False,blank=False)


    def __str__(self):
        return self.firstname
