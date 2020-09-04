from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate

from .forms import LoginForm

# Create your views here.


def login_view(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      user = authenticate(
        request,
        username=data.get('username'),
        password=data.get('password'),
      )
      if user:
        login(request, user)
        return HttpResponseRedirect(reverse('homepage'))
  form = LoginForm()
  return render(
    request,
    'login.html',
    {'form': form},
  )


def logout_view(request):
  logout(request)
  return HttpResponseRedirect(reverse('homepage'))