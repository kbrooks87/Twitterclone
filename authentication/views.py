from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.views.generic import TemplateView

from .forms import LoginForm

# Create your views here.

class LoginView(TemplateView):


  def get(self, request):
    form = LoginForm()
    return render(
      request,
      'login.html',
      {'form': form},
      )

  def post(self, request):
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


def logout_view(request):
  logout(request)
  return HttpResponseRedirect(reverse('homepage'))