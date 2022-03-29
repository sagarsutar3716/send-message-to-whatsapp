from twilio.rest import Client
from send_whatsapp_msg.settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages

# Create your views here.


def home(request):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    order_details = {
    'amount': '15000',
    'item': 'Laptop',
    'date_of_delivery': '028/03/2022',
    'address': 'No 1, CMBP Navi Mumbai'
	}

    if request.method == 'POST':
        user_whatsapp_number = request.POST['send_msg']

        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body='Your {} order of {} has shipped and should be delivered on {}. Details: {}'.format(
                order_details['amount'], order_details['item'], order_details['date_of_delivery'],
                order_details['address']),
            to='whatsapp:+{}'.format(user_whatsapp_number)
        )

        print(user_whatsapp_number)
        
        messages.add_message(request, messages.INFO,"Message Send Successfully...")
        return redirect('/')

    return render(request,"index.html")