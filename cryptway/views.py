from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def blog(request):
    return render(request, 'blog.html', {})

def contact(request):
    if request.method == 'POST':
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        email_address = request.POST['email']
        phone_number = request.POST['phone-number']
        message = request.POST['message']
        feedback_mode = request.POST.get('radio')
        if int(feedback_mode) == 0:
            feedback_mode = "phone"
        elif int(feedback_mode) == 1:
            feedback_mode = "email"
        else:
            feedback_mode == "other"

        try:
            print(feedback_mode)
            send_mail(name, message, email, ['anyaogupeter601@gmail.com'], fail_silently=True)
        except Exception:
            pass
        return render(request, 'contact.html', {'first_name':first_name})

    return render(request, 'contact.html', {})

def single_blog(request):
    return render(request, 'single-blog.html', {})

def signup(request):
    return render(request, 'signup.html', {})

def signin(request):
    return render(request, 'signin.html', {})