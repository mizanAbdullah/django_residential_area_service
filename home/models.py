from django.db import models

# Create your models here.
class Rent(models.Model):
    title=models.CharField(max_length=1000)
    total_bedroom=models.IntegerField()
    total_washroom=models.IntegerField()
    total_squarefeets=models.IntegerField()
    house_image_1=models.ImageField("images/")
    house_image_2=models.ImageField("images/")
    house_image_3=models.ImageField("images/")
    montly_rent=models.IntegerField()
    mobile_number=models.IntegerField()
    division=models.CharField(max_length=1000)
    district=models.CharField(max_length=1000)
    address_details=models.CharField(max_length=1000)
    datetime = models.DateField(null=True, blank=True)
    
    

class Teacher(models.Model):
    name=models.CharField(max_length=1000)
    address=models.CharField(max_length=1000)
    mobile_number=models.CharField(max_length=1000)
    image=models.CharField(max_length=1000)
    email=models.EmailField()
    school_name=models.CharField(max_length=1000)
    ssc_result=models.CharField(max_length=1000)
    college_name=models.CharField(max_length=1000)
    Hsc_result=models.CharField(max_length=200)
    other_degree=models.TextField()
    datetime = models.DateField(null=True, blank=True)

    


