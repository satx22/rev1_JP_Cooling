# home/views.py

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponseRedirect
from .forms import ContactForm, SpecialOfferEmailForm

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def acinstallation(request):
    return render(request, 'acinstallation.html')

def antimicrobialfogging(request):
    return render(request, 'antimicrobialfogging.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            service = form.cleaned_data['service']
            message_content = form.cleaned_data['message']

            # Email content
            message = f"Name: {name}\nPhone: {phone}\nService: {service}\nMessage: {message_content}"
            
            # Send email
            send_mail(
                f"New contact form submission from {name}",
                message,
                email,
                ['jpcoolingandheat@gmail.com'],  # Change to your email or list of emails
                fail_silently=False,
            )

            # Display success message
            messages.success(request, 'Your appointment request has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def ductlessminisplits(request):
    return render(request, 'ductlessminisplits.html')

def MaintenanceandRepair(request):
    return render(request, 'MaintenanceandRepair.html')

def services(request):
    return render(request, 'services.html')

def tuneup(request):
    return render(request, 'tuneup.html')

# Special Offers

def special_offer(request):
    if request.method == 'POST':
        form = SpecialOfferEmailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('special_offer')
    else:
        form = SpecialOfferEmailForm()
    return render(request, 'home/special_offer.html', {'form': form})
