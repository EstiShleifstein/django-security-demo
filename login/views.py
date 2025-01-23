from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm, CommentForm
from .models import Comment
from django.contrib.auth import get_user_model

def home(request): 
  username = request.user.username
  return render(request, "home.html", {'username':username})

def register(request):
  if request.method == "POST":
    form = RegisterForm(request.POST)
    if form.is_valid():
      user = form.save()  # This HASHES the password and saves the user
      username = form.cleaned_data.get('username')
      raw_password = form.cleaned_data.get('password1') # Raw password used only for authentication
      user = authenticate(username=username, password=raw_password) # Authenticate user
      if user is not None:
        login(request, user)
        return redirect("/")
      else:
        return render(request, "register.html", {"form":form})
    else:
      return render(request, "register.html", {"form":form})

  else:
    form = RegisterForm()
    return render(request, "register.html",{"form":form})
  

def csrf_demo(request):
  return render(request, "csrf-demo.html", {})

def authentication_demo(request):
  return render(request, "authentication-demo.html", {})

def sql_demo(request):
  return render(request, "sql-demo.html", {})

def xss_demo(request):
  form = CommentForm()

  if request.method == "POST":
    form = CommentForm(request.POST)
    if form.is_valid():
      secure_comment = form.cleaned_data['secure_comment']
      unsecure_comment = form.cleaned_data['unsecure_comment']
    return render(request, "xss-demo.html", {'form': form, 'secure_comment': secure_comment, 'unsecure_comment':unsecure_comment})
  return render(request, "xss-demo.html", {'form': form})

def admin_demo(request):
  return render(request, "admin-patchup-demo.html", {})

def nav_next(request):
  nav_sequence = ['home', 'authentication_demo', 'xss_demo', 'csrf_demo', 'sql_demo', 'admin_demo']
  current_index = request.session.get("cur_template_index", 0)
  next_template_index = current_index + 1  
  
  if next_template_index < len(nav_sequence):
    next_template = nav_sequence[next_template_index]
    request.session["cur_template_index"] = next_template_index
  else:
    next_template = nav_sequence[0]
    request.session["cur_template_index"] = 0

  return redirect(next_template)

