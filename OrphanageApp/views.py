from django.shortcuts import render,redirect,get_object_or_404
from . forms import UserForm, EventBookingForm, VolunteerForm,OrphanForm,OrpForm,Add_orphanForm,AddoptentForm,EmailForm
from . models import User, Volunteer,Confirmed_events,Add_orphan,EventBooking,Orphanage,AdoptentLogin
from django.contrib import auth
from django.core.mail import send_mail
# Create your views here.

def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            to_email = form.cleaned_data['to_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = 'therasaorphanage@gmail.com'  
            recipient_list = [to_email]
            send_mail(subject, message, from_email,recipient_list , fail_silently=False)

        
            return redirect('/')
    else:
        form = EmailForm()

    return render(request, 'html/email_form.html', {'form': form})

def home(request):
    volunteers = Volunteer.objects.all()
    confirmed_events=Confirmed_events.objects.all()
    if request.method == "POST":
        t = VolunteerForm(request.POST)
        if t.is_valid():
            t.save()
            return redirect('/')
    form = VolunteerForm()
    return render(request, 'html/home.html', {"confirmed_events":confirmed_events,'volunteers': volunteers})

def vhome(request):
    volunteers = EventBooking.objects.all()
    if request.method == "POST":
        t = VolunteerForm(request.POST)
        if t.is_valid():
            t.save()
            return redirect('/vhome')
    return render(request,'html/volenteer_home.html',{'volunteers':volunteers})

def about(request):
	return render(request,'html/about.html')

# def accept(request,id):
#     v=Volunteer.objects.get(id=id)
#     ce=Confirmed_events(name=v.name,contact=v.contact,event_date=v.event_date,aadhar=v.aadhar,availability=v.availability,subject=v.subject,skills=v.skills,email=v.email)
#     ce.save()
#     v.delete()
#     ce = Confirmed_events.objects.all()
#     return redirect('/vhome')
#     return render(request, 'html/home.html', {'confirmed_events': confirmed_events})

def accept(request, id):
    v = EventBooking.objects.get(id=id)
    
    ce = Confirmed_events(name=v.name, contact=v.contact, event_date=v.event_date, aadhaar=v.aadhaar, availability=v.availability, subject=v.subject, skills=v.skills, email=v.email)
    ce.save()
    v.delete()
    confirmed_events = Confirmed_events.objects.all()
    return render(request, 'html/home.html', {'confirmed_events': confirmed_events})

def contact(request):
	return render(request,'html/contact.html')

def register(request):
	if request.method == "POST": 
	    g = UserForm(request.POST)
	    if g.is_valid():
	    	g.save()
	    	return redirect('/lgo')
	g = UserForm()
	return render(request,'html/register.html',{'t':g})

def login(request):
	if request.method == "POST": 
	    g = UserForm(request.POST)
	    if g.is_valid():
	    	g.save()
	    	return redirect('/')
	g = UserForm()
	return render(request,'html/login.html')


def volenteer_login(request):
    error = None  
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/', error='no')
        else:
            error = 'yes'
    else:
        form = VolunteerForm()

    return render(request, 'html/volenteer_login.html', {'form': form, 'error': error})







# def addoptentlogin(request):
#     if request.method == "POST":
#         g = AddoptentForm(request.POST)
#         if g.is_valid():
#             g.save()
#             medical_report = request.FILES.get('medical_report')
#             return redirect('/')
#     g = AddoptentForm()
#     return render(request,'html/addoptentlogin.html',{'t':g})

def addoptentlogin(request):
    
    if request.method == "POST":
        form = AddoptentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AddoptentForm()

    return render(request, 'html/addoptentlogin.html', {'t': form})





def adoptent_login_list(request):
    records = AdoptentLogin.objects.all()
    return render(request, 'html/adoptent_login_list.html', {'records': records})



def delete_record(request, record_id):
    try:
        record = AdoptentLogin.objects.get(pk=record_id)
        record.delete()
    except AdoptentLogin.DoesNotExist:
        pass  # Handle the case where the record doesn't exist
    return redirect('adoptent_login_list')  









def event_booking(request):
    error = None  
    if request.method == 'POST':
        form = EventBookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/', error='no')
        else:
            error = 'yes'
    else:
        form = EventBookingForm()

    return render(request, 'html/event_booking.html', {'form': form, 'error': error})

    
def event_booking_success(request):
    return render(request, 'html/event_booking_success.html')




    
def accepted_events(request):
    events=Confirmed_events.objects.all()

    return render(request, 'html/accepted_events.html',{"confirmed_events":events})




def edit_volunteer(request, id):
    volunteer = EventBooking.objects.get(id= id)
    
    if request.method == 'POST':
        form = VolunteerForm(request.POST, instance=volunteer)
        if form.is_valid():
            form.save()
            return redirect('/')  
    else:
        form = VolunteerForm(instance=volunteer)

    return render(request, 'html/edit_volunteer.html', {'form': form})




def delete_volunteer(request, id):
    volunteer = EventBooking.objects.get(id=id)
    #volunteer = get_object_or_404(Volunteer, id=id)
    if request.method == 'POST':
        volunteer.delete()
        return redirect('/')  

    return render(request, 'html/delete_volunteer.html', {'volunteer': volunteer})





def delete_confirmed_event(request, id):
    confirmed_event = Confirmed_events.objects.get(id=id)
    if request.method == 'POST':
        confirmed_event.delete()
        return redirect('/')  # Redirect to the volunteer home page or any other desired page

    return render(request, 'html/delete_confirmed_event.html', {'confirmed_event': confirmed_event})



def add_orphan(request):
    ad=Add_orphan.objects.all()
    if request.method == 'POST':
        form = OrphanForm(request.POST)
        if form.is_valid():
            form.save()
            # data.save()
            return redirect('/')  # Redirect to orphanage website
    else:
        form = OrphanForm()
    return render(request, 'html/add_orphan.html', {'form': form,"h":ad})


def edit_orphan(request, id):
    volunteer = Add_orphan.objects.get(id= id)
    
    if request.method == 'POST':
        form = OrphanForm(request.POST, instance=volunteer)
        if form.is_valid():
            form.save()
            return redirect('add_orphan')  
    else:
        form = OrphanForm(instance=volunteer)

    return render(request,'html/add_orphan.html', {'form': form,"h":None})


def delete_orphan(request,id):
    volunteer = Add_orphan.objects.get(id= id)
    volunteer.delete()
    return redirect('add_orphan')


def Add_orphanform(request):
    h = OrpForm.objects.filter(id=request.user.id)
    if request.method == 'POST':
        form = Add_orphanform(request.POST)
        if form.is_valid():
            form.save()


            return redirect('/')  # Redirect to a success page or any other desired URL
    else:
        form = Add_orphan()
    return render(request, 'html/add_orphanform.html', {'form': form,'s':h})



def adorphan(request):
    orphans = Add_orphanForm()
    return render(request, 'addorphan.html', {'orphans': orphans})



def orphan_details(request):
    j = Add_orphan.objects.all()
    return render(request, 'html/orphans_details.html', {'h': j})

# Edit orphan view
# def edit_orphan(request, id):
#     orphan = get_object_or_404(Add_orphan, id=id)

#     if request.method == 'POST':
#         form = AddOrphanForm(request.POST, instance=orphan)
#         if form.is_valid():
#             form.save()
#             return redirect('/')

#     form = AddOrphanForm(instance=orphan)
#     return render(request, 'edit_orphan.html', {'form': form, 'orphan': orphan})

# Delete orphan view
# def delete_orphan(request, id):
#     orphan = get_object_or_404(Add_orphan, id=id)

#     if request.method == 'POST':
#         orphan.delete()
#         return redirect('/')

#     return render(request, 'delete_orphan.html', {'orphan': orphan})



def orphcr(request):
    v = User.objects.get(id=request.user.id)
    if request.method=="POST":
        h = OrpForm(request.POST)
        if h.is_valid():
            w = h.save(commit=False)
            w.Msc_id = request.user.id
            v.has_orphanage = 1
            w.save()
            v.save()
            return redirect('/')
    h = OrpForm()
    return render(request,'html/orphanage.html',{'b': h})


def user_login(request):
    if request.method=="POST":
        u=request.POST["username"]
        p=request.POST["password"]
        user=auth.authenticate(request,username=u,password=p)
        if user is not None:
            auth.login(request,user)
            return redirect('hm')
        else:
            pass
    return render(request,"html/login.html")





def requested_events(request):
    E=EventBooking.objects.all()
    return render(request,'html/volenteer_home.html',{"volunteers":E})





