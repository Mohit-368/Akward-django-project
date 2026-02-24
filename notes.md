user-mohit pass-acer123
use pip freeze > requiremnt.txt to create a requirement file
to create a admin or super user use command[python manage.py createsuperuser]
from django.contrib.auth.models import User this command is used to import user data in models so that we can change or modify it
user=models.ForeignKey(User,on_delete=models.CASCADE)?????????????????????
models bnane k baad usko admin m register krte h --- from .models import Post admin.site.register(Post)
from django.shortcuts import get_object_or_404 get request ko ese import krte h ,
forms aur modls banae k baad usko views m import kro taaki uspe page bna sko
def Post_list(request): posts=Post.objects.all().order_by('-created_at') return render(request ,'post_list.html', {'posts':posts}) ese database ko ek view m send krte h
to chaeck whether user is logged in use user.is_autenticated

# authentication :

## this is how we should protect pages :

```python
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, "dashboard.html")

```

## 1. basic

1. Register

```python
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "register.html", {"form": form})
```

2. Login

```python
from django.contrib.auth import authenticate, login

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
    return render(request, "login.html")
```

3. logout

```python
from django.contrib.auth import logout

def user_logout(request):
    logout(request)
    return redirect("login")

```

improvement:

1. logout conformation page
2. success message on registration
