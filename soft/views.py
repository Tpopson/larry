from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings


from .models import *
from .forms import ContactForm
# Create your views here.
def index(request):
    company = CompanyProfile.objects.get(pk=1)
    service = Service.objects.all().order_by('-id')
    return render(request, 'index.html',{
        'company':company,
        'service':service,
        })


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

        sender_name = request.POST['name']
        sender_email = request.POST['email']
        sender_msg = request.POST['message']
        email = EmailMessage(
            'You contacted Us',#subject
            f'Dear {sender_name}! thank you for contacting us,we received your message: \n \n {sender_msg} \n \n our customer service agents will contact you shortly.Thank you.',#message
            settings.EMAIL_HOST_USER,#host email
            [sender_email] #sender
            )

        email.fail_silently = True
        email.send()
        messages.success(request, 'Your message has been sent successfully')
        return redirect('index')
        
    return render(request, 'index.html')