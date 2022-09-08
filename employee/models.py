from email.policy import default
from django.db import models
from birthday import BirthdayField 
from django.core.validators import RegexValidator
from django_countries.fields import CountryField

# Create your models here.
class Employee(models.Model): 

    #Department's 
    DEPARTMENTT = ( 
        ('D1','DEPARTMENT1'), 
        ('D2','DEPARTMENT2'), 
        ('D3','DEPARTMENT3'), 
        ('D4','DEPARTMENT4'), 
        ('D5','DEPARTMENT5'), 
        ('D6','DEPARTMENT6'), 
    )  

    #STATE 
    STATES = (
        ('Active','ACTIVE'), 
        ('Leave_count','LEAVE COUNT'), 
        ('On_leave','ON LEAVE')
    )

    id = models.AutoField(primary_key=True) 
    Name = models.CharField(max_length=30)
    Surname = models.CharField(max_length=30)
    DOB = BirthdayField(help_text="YY-MM-DD") 
    DOJ = models.CharField(max_length=10) 
    Department = models.CharField(max_length=100,choices=DEPARTMENTT) 
    Post = models.CharField(max_length=10) 
    Address =  models.CharField(max_length=50) 
    country = CountryField(default='IN')
    City = models.CharField(max_length=25,default='') 
    Zip = models.CharField(
        max_length=5,
        validators=[RegexValidator(r'\d\d\d\d\d')] , 
        help_text='Zip Code',
        default=''
    )
    State = models.CharField(max_length=100,choices=STATES,default='Leave_count')

    def __str__(self):
        return "{} {} - {}".format(self.Name,self.Surname,self.id)
