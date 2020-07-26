from django.shortcuts import render
import os
from twilio.rest import Client
import requests

number = "hi"

def index(request):
    if request.method == 'POST':
        number = request.POST.get('textfield', None)
        client = Client()
        from_whatsapp_number = 'whatsapp:+14155238886'
        to_whatsapp_number = 'whatsapp:+91'+number
        client.messages.create(body='Thanks for being our valuable customer! Please rate us between 1 to 5.', from_=from_whatsapp_number, to=to_whatsapp_number)
        return render(request, 'thanks.html')
    return render(request, 'index.html')

def thanks(request):
    return render(request, 'thanks.html')

def check_ratings(request):
    response = requests.get('https://api.twilio.com/2010-04-01/Accounts/AC3b6a699c4df765e6707f23a4ac084311/Messages.json')
    data = response.json()
    print(data)