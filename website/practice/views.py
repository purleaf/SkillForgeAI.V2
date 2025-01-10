from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.conf import settings
from .forms import UserRegisterForm, SignupForm
from django.contrib.auth import login
import json
from django.http import JsonResponse
from .quiz_gen import QuizGeneration


def main_page(request):
    return render(request, "main.html")


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.email
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('main_page')
        else:
            return render(request, 'account/login1.html', {
                'form': form,
                'signup_mode': True
            })
    else:
        form = SignupForm()
        return render(request, 'account/login1.html', {
            'form': form,
            'signup_mode': True
        })


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            messages.error(request, "Invalid email or password.")
            return redirect('login')
    return render(request, 'account/login1.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def toefl_page(request):
    return render(request, "toefl_page.html")


def quiz_api_view(request):
    generator = QuizGeneration()
    quiz_data = generator.generate_response()
    quiz_dict = quiz_data.dict()
    return JsonResponse(quiz_dict, safe=False)


def ielts_page(request):
    return render(request, "IELTS.html")


@login_required
def toefl_reading(request):
    generator = QuizGeneration()
    quiz = generator.generate_response()
    json_f = json.loads(quiz.json())
    context = {"passages": json_f["passages"]}
    return render(request, "toefl_reading-v2.html", context)


@login_required
def ielts_writing(request):
    return render(request, "ielts_writing.html")


@login_required
def toefl_listening(request):
    return render(request, "toefl_listening.html")


@login_required
def toefl_writing(request):
    return render(request, "toefl_writing.html")


@login_required
def toefl_speaking(request):
    return render(request, "toefl_speaking.html")


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Account created for {user.username}!')
            return redirect('main_page')
        else:
            messages.error(request, f'Please corct the error below.')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def account_settings(request):
    return render(request, 'account/account_settings.html')

# @login_required
# def account_settings(request):
#     return render(request, 'account_setings.html')
