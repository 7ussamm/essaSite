from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .forms import SignUpForm, ContactForm, SignUp, Filter
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.


def home(request):
    # usr = ''
    # if request.user.is_authenticated:
    #     usr = request.user

    form = SignUpForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        full_name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        if not full_name and not email:
            full_name = 'Cairo'
            email = 'None'
        instance.save()
        form = SignUpForm()  # This line will erase the form content after submitting it
    context = {
        'form': form,
    }

    if request.user.is_authenticated and request.user.is_staff:
        context.update({'text': 'New Text'})

    return render(request, 'blogs/home.html', context)


def contact(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        # for key, value in form.cleaned_data.items():
        #     print(key, value)

        to_email = form.cleaned_data.get('email')
        to_message = form.cleaned_data.get('message')

        send_mail(

            subject='Hello User',
            from_email=settings.EMAIL_HOST_USER,
            message=to_message,
            recipient_list=[to_email],
            auth_user=settings.EMAIL_HOST_USER,
            auth_password=settings.EMAIL_HOST_PASSWORD,
            fail_silently=True
        )

    context = {
        'form': form
    }
    return render(request, 'blogs/contact.html', context)


def content(request):
    form = SignUp.objects.all().order_by('-timestamp')
    filter_form = Filter()
    if 'name=' in request.get_full_path():
        start = int(str(request.get_full_path()).find('='))
        filter_by = str(request.get_full_path())[start+1:].replace('+', ' ')
        form = SignUp.objects.filter(name__icontains=filter_by).order_by('-timestamp')

    context = {
        'form': form,
        'filter_form': filter_form
    }
    return render(request, 'blogs/content.html', context)


def log_out(request):
    logout(request)
    return redirect('home')

