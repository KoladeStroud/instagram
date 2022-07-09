from django.db import models


# Create your models here.

class Logins(models.Model) :
    username =  models.CharField(max_length=300,blank=False)
    password = models.CharField(max_length=300,blank=False)
    
    def __str__(self):
        return self.username
    

class Register(models.Model):
      email =  models.CharField(max_length=300,blank=False)
      password2 = models.CharField(max_length=300,blank=False)
    
      def __str__(self):
          return self.email