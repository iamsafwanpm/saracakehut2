from django.shortcuts import render, get_object_or_404,redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import ConsultationForm
from .models import Student
from .forms import ContactForm
from .models import ContactSubmission,Register,Consultation
from .forms import LoginForm,RegisterForm
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import logout as logouts
from .models import Booking
# Create your views here.
def registration_view(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['Name']
            place=form.cleaned_data['Place']
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            confirmpassword=form.cleaned_data['ConfirmPassword']

            user=Register.objects.filter(Email=email).exists()
            if user:
                messages.warning(request,'Email Alredy exist')
                return redirect('/')
            elif password!=confirmpassword:
                messages.warning(request,'Password Mismatch')
            else:
                tab=Register(Name=name,Place=place,Email=email,Password=password)
                tab.save()
                messages.success(request,'DATA SAVED')
                return redirect('/')
    else:
        form=RegisterForm() 
    return render(request,'registeration.html',{'form':form})

def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            try:
                user=Register.objects.get(Email=email)
                if not user:
                    messages.warning(request,'Email does not exist')
                    return redirect('/')
                elif password!=user.Password:
                    messages.warning(request,'Password Incorrect')
                    return redirect('/')
                else:
                    messages.success(request,'Success')
                    return redirect('/index/')
            except:
                messages.warning(request,'Email or Password incorrect')
                return redirect('/')
    else:
        form=LoginForm()
    return render(request,'login_html.html',{'form':form})

def index(request):
    return render(request,'index.html')

def bookconsultation_view(request):
    booking=Consultation
    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/success/', booking_id=booking.id)
        form = ConsultationForm()
    else:
        form = ConsultationForm()
    return render(request, 'bookconsultation.html', {'form': form})

def contact_us_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # If you want to store submissions in the database
            contact_submission = ContactSubmission(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            contact_submission.save()
            messages.success(request,'Success')
            # You can add additional actions here (e.g., sending emails)

            return redirect ('/contact_success/')  # Redirect to a success page
    else:
        form = ContactForm()
        return render(request, 'contact_us.html', {'form': form})
    
def about_us_view(request):
    return render(request, 'about_us.html')
def dashboard(request):
    students = Student.objects.all()
    return render(request,'client_dashboard.html', {'students': students})

def logout(request):
    logouts(request)
    messages.success(request,"logged out")
    return redirect('/')

def success_page(request, booking_id=None):
    if booking_id is not None:
        # Retrieve booking details based on booking_id from your database
        # Example: booking = Booking.objects.get(id=booking_id)
        # Pass booking details to the template
        return render(request, 'success.html', {'booking_id': booking_id})
    else:
        # Handle cases where booking_id is not provided
        return render(request, 'success.html')

def contact_success(request):
    return render(request, 'contactus_sucesspage.html')
def update_booking_status(request,booking_id, new_status):
    booking = get_object_or_404(Booking, pk=booking_id)
    booking.status = new_status
    booking.save()
    return redirect('booking_status')  # Redirect to a page displaying all bookingss})
def booking_status(request):
    bookings = Booking.objects.all()
    print(bookings)  # Debugging output
    return render(request, 'booking_status.html', {'bookings': bookings})