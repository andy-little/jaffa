from django.shortcuts import render
import smtplib
import os
import json

# Create your views here.
def index(request):
    return render(request, 'main/index.html', {'home': True})

def setups(request):
    return render(request, 'main/setups.html', {'setups': True})

def equipment(request):
    return render(request, 'main/equipment.html', {'equipment': True})


def about(request):
    return render(request, 'main/about.html', {'about': True})


def contact(request):
    if request.method == 'POST':
        with open('/etc/config.json') as config_file:
            config = json.load(config_file)
            EMAIL_ADDRESS = config.get('EMAIL_USER') 
            EMAIL_PASS = config.get('EMAIL_PASS')
            name = request.POST['name']
            sender = request.POST['email']
            contents = request.POST['message']
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()
                smtp.login(EMAIL_ADDRESS, EMAIL_PASS)
                subject = f'Portfolio Contact Form From: {name}'
                body = contents

                msg = f'Subject: {subject}\n\n{body}'
                smtp.sendmail(EMAIL_ADDRESS, 'andy.little@hotmail.co.uk', f'{msg}\nSender: {sender}')
        return render(request, 'main/contact.html', {'contact' : True, 'sent' : True})
    return render(request, 'main/contact.html', {'contact' : True})

