from django.db import models

# Create your models here.
class school(models.Model):
    scname=models.CharField(max_length=100,primary_key=True)
    scprincipal=models.CharField(max_length=100)
    sclocation=models.CharField(max_length=100)
    
    def __str__(self):
        return self.scname

class student(models.Model):
    scname=models.ForeignKey(school,on_delete=models.CASCADE)
    studentname=models.CharField(max_length=100)
    sid=models.IntegerField(primary_key=True)

    def __str__(self):
        return self.studentname
    
    
