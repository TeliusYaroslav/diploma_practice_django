from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db.utils import IntegrityError
from django.contrib.auth.password_validation import validate_password
from django.views.decorators.csrf import csrf_exempt
import re

@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password-2')
        errors = {}
        if not username:
            errors['username_error'] = 'Ім’я користувача є обов’язковим.'
        elif not re.match(r'^[a-zA-Zа-яА-ЯёЁіІїЇєЄ]+$', username):
            errors['username_error'] = 'Ім’я користувача може містити тільки букви.'
        if not email:
            errors['email_error'] = 'Електронна пошта є обов’язковою.'
        else:
            try:
                validate_email(email)
            except ValidationError:
                errors['email_error'] = 'Невірний формат електронної пошти.'
        if not password:
            errors['password_error'] = 'Пароль є обов’язковим.'
        elif len(password) < 6:
            errors['password_error'] = 'Пароль має бути не менше 6 символів.'
        elif re.search(r'[.,\-+=]', password):
            errors['password_error'] = 'Пароль не повинен містити ., -=+= символів.'
        if password != password2:
            errors['password2_error'] = 'Паролі не співпадають.'
        if errors:
            return render(request, 'fitnes_studio/register.html', errors)
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            login(request, user)
            return redirect('main')
        except IntegrityError:
            errors['username_error'] = 'Ім’я користувача вже існує.'
            return render(request, 'fitnes_studio/register.html', errors)

    return render(request, 'fitnes_studio/register.html')

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            return render(request, 'fitnes_studio/login.html', {'error_message': 'Невірні дані.'})
    return render(request, 'fitnes_studio/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def about_us(request):
    return render(request, 'fitnes_studio/about_us.html')

def gallery(request):
    return render(request, 'fitnes_studio/gallery.html')

def appointment(request):
    return render(request, 'fitnes_studio/appointment.html')

def contacts(request):
    return render(request, 'fitnes_studio/contacts.html')

def main(request):
    return render(request, 'fitnes_studio/main.html')
