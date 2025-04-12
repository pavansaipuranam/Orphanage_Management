from django.contrib.auth.forms import UserCreationForm
from django import forms
from . models import User, EventBooking,Volunteer,Add_orphan,Orphanage,AdoptentLogin

class UserForm(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":
		"form-control my-2","placeholder":"Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":
		"form-control my-2","placeholder":"Confirm Password"}))
	class Meta:
		model = User
		fields = ["username","uid"]
		widgets = {
		"username":forms.TextInput(attrs={
		"class":"form-control my-2",
        "placeholder":"Username",
			}),
        "uid":forms.TextInput(attrs={
		"class":"form-control my-2",
        "placeholder":"Unique Id",
			}),
		}
class EventBookingForm(forms.ModelForm):
    class Meta:
        model = EventBooking
        fields = ['name', 'contact', 'aadhaar', 'email', 'event_date', 'subject', 'availability', 'skills']
        widgets = {
		"name":forms.TextInput(attrs={
		"class":"form-control my-2",
        "placeholder":"Name",
			}),
        'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Number', 'required': 'true'}),
        'aadhaar': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Aadhaar Number'}),
        'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email ID', 'required': 'true'}),
        'event_date': forms.DateInput(attrs={'class': 'form-control', 'required': 'true','placeholder' : "DD/MM/YYYY"}),
        'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Subject', 'required': 'true'}),
        'availability': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Time'}),
        'skills': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Skills/Interests'}),
		}

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['name', 'contact', 'aadhaar', 'email', 'event_date', 'subject', 'availability', 'skills']
        widgets = {
		"name":forms.TextInput(attrs={
		"class":"form-control my-2",
        "placeholder":"Name",
			}),
        'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Number', 'required': 'true'}),
        'aadhaar': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Aadhaar Number'}),
        'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email ID', 'required': 'true'}),
        'event_date': forms.DateInput(attrs={'class': 'form-control','placeholder': 'DD/MM/YYYY', 'required': 'true'}),
        'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Subject', 'required': 'true'}),
        'availability': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Availability'}),
        'skills': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Skills/Interests'}),
		}



class Add_orphanForm(forms.ModelForm):
    class Meta:
        model = Add_orphan
        fields = ['name', 'gender', 'age', 'father_name', 'mother_name']
        

class OrphanForm(forms.ModelForm):
    class Meta:
        model = Add_orphan
        fields = ['name', 'age', 'gender','father_name','mother_name','date_of_birth']
        widgets = {
		"name":forms.TextInput(attrs={
		"class":"form-control my-2",
        "placeholder":"Name",
			}),

		"age":forms.TextInput(attrs={
		"class":"form-control my-2",
        "placeholder":"age",
			}),

		"gender":forms.TextInput(attrs={
		"class":"form-control my-2",
        "placeholder":"gender",
			}),

		"father_name":forms.TextInput(attrs={
		"class":"form-control my-2",
        "placeholder":"Father Name",
			}),
		"mother_name":forms.TextInput(attrs={
		"class":"form-control my-2",
        "placeholder":"Mother Name",
			}),
		"date_of_birth":forms.DateInput(attrs={
		"class":"form-control my-2",
		"type":"date_of_birth",
		"placeholder":"MM/DD/YYYY",
			}),
		}


class OrpForm(forms.ModelForm):
	class Meta:
		model = Orphanage
		fields = ["Oname","chairman","mobile","Land_line","contact_email","Olocation","established_date"]
		widgets = {
		"Oname":forms.TextInput(attrs={
		"class":"form-control my-2",
        "placeholder":"Orphanage Name",
			}),
		"chairman":forms.TextInput(attrs={
		"class":"form-control my-2",
        "placeholder":"Chairman Name",
			}),
		"mobile":forms.TextInput(attrs={
		"class":"form-control my-2",
        "placeholder":"Mobile Mumber",
			}),
		"Land_line":forms.TextInput(attrs={
		"class":"form-control my-2",
        "placeholder":"Land_line Number",
			}),
		"contact_email":forms.EmailInput(attrs={
		"class":"form-control my-2",
        "placeholder":"Email Id",
			}),
		"Olocation":forms.TextInput(attrs={
		"class":"form-control my-2",
        "placeholder":"Address",
			}),
		"established_date":forms.DateInput(attrs={
		"class":"form-control my-2",
		"type":"date",
			}),



		}



class AddoptentForm(forms.ModelForm):
    class Meta:
        model = AdoptentLogin
        fields = ['full_name', 'contact_number', 'aadhaar_number','email', 'have_child','occupation','monthly_income','medical_report']
        




class EmailForm(forms.Form):

    to_email = forms.EmailField(label="Recipient's Email", widget=forms.TextInput(attrs={'class': 'form-control',"placeholder":"To",
}))
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control',"placeholder":"Subject"}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',"placeholder":"Drop Your Message here...."}))





