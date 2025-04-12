from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.
class User(AbstractUser):
	c = [
	    ('0','Guest'),
	    ('1','Adoptent'),
	    ('2','Manager'),
	]
	role_type = models.CharField(max_length=5,choices=c,default='0')
	uid = models.CharField(max_length=15)
	is_addoptent = models.BooleanField(default=False)
	has_orphanage = models.BooleanField(default=False)

class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    aadhaar = models.CharField(max_length=12, null=True, blank=True)
    email = models.EmailField()
    event_date = models.DateField()
    subject = models.CharField(max_length=100)
    availability = models.CharField(max_length=100, null=True, blank=True)
    skills = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class Confirmed_events(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    aadhaar = models.CharField(max_length=12, null=True, blank=True)
    email = models.EmailField()
    event_date = models.DateField()
    subject = models.CharField(max_length=100)
    availability = models.CharField(max_length=100, null=True, blank=True)
    skills = models.CharField(max_length=100, null=True, blank=True)




class AdoptentLogin(models.Model):
    full_name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=10)
    aadhaar_number = models.CharField(max_length=12, null=True, blank=True)
    email = models.EmailField(default='')
    have_child = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50,null=True,default='')
    monthly_income = models.CharField(max_length=20,null=True)
    medical_report = models.FileField(upload_to='medical_reports/', blank=True, null=True)
    def __str__(self):
       return self.name;




class EventBooking(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15,default='')
    aadhaar = models.CharField(max_length=12, null=True, blank=True)
    email = models.EmailField(default='')
    event_date = models.DateField()
    subject = models.CharField(max_length=100,default='')
    availability = models.CharField(max_length=100, null=True, blank=True)
    skills = models.CharField(max_length=100, null=True, blank=True)



class Add_orphan(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    age = models.PositiveIntegerField(default='')
    father_name = models.CharField(max_length=50,null=True)  
    mother_name = models.CharField(max_length=50,null=True)  
    date_of_birth = models.DateField(null=True)
    



class AddoptentForm(models.Model):
    Alocation = models.CharField(max_length=100)
    Adsg = models.CharField(max_length=100,null=True,blank=True)
    mobile = models.CharField(max_length=100)
    Asd = models.OneToOneField(User,on_delete=models.CASCADE)



class Orphanage(models.Model):
    Oname = models.CharField(max_length=100)
    chairman = models.CharField(max_length=100)
    Olocation = models.CharField(max_length=200)
    mobile = models.CharField(max_length=100)
    Land_line = models.CharField(max_length=100)
    contact_email = models.EmailField()
    established_date = models.DateField()
    Msc = models.OneToOneField(User,on_delete=models.CASCADE)


