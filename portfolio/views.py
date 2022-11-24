from typing import TextIO
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def about(request):

    return render(request, 'about.html')



def work(request):
    return render(request, 'work.html')

def contact(request):
    if request.method == 'POST':
        
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        data={
            
            'email':email,
            'subject' : subject,
            'message':message
        }
        message = '''
        Nuevo mensaje : {}
        
        From : {}
        
        '''.format(data['message'], data['email'])
        send_mail(data['subject'], message, '', ['santiagourban26@gmail.com'])
        return redirect('/thanku/')
        
        
    return render(request, 'contact.html', {})

def write_to_file(params):
    with open('database.txt', mode='a') as database:
        email =params["email"]
        subject =params["subject"]
        message =params["message"]
        file=database.write(f'\n {email}, {subject}, {message}')




def submit(request):
    
        return render(request, 'thanku.html')




