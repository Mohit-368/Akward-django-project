from django.shortcuts import render  
# render ka use template (html file) ko browser me dikhane ke liye hota h

from .models import Post  
# yaha hum apna Post model import kar rahe h taaki database se data nikal sake

from .forms import Postfrom  , UserRegistrationForm
# yaha hum apna form import kar rahe h jo user se data lega

from django.shortcuts import get_object_or_404 , redirect  
# get_object_or_404: agar object mile to dega warna 404 error
# redirect: kisi dusre url par bhejne ke liye
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.


def index(request):
    # simple homepage view h jo sirf index.html ko render karega
    return render(request,'index.html')


def post_list(request):
    # Post model se saare posts nikal rahe h
    # .all() -> sabhi records
    # .order_by('-created_at') -> latest post upar dikhane ke liye descending order
    posts = Post.objects.all().order_by('-created_at') 
    
    # post_list.html ko posts data ke sath bhej rahe h
    return render(request ,'post_list.html', {'posts':posts})

@login_required
def post_create(request):
    # is function ka kaam h user ko form dena
    # do cases handle karne h:
    # 1) user first time page open kare (GET request)
    # 2) user form fill karke submit kare (POST request)

    if request.method == 'POST':
        # agar form submit hua h to POST method hoga
        
        form = Postfrom(request.POST , request.FILES)
        # request.POST -> text data (title, content etc)
        # request.FILES -> image ya file upload ke liye
        
        if form.is_valid():
            # ye line sab validation check karti h (security + required fields etc)
            
            posts = form.save(commit=False)
            # commit=False ka matlab abhi database me save mat karo
            # kyuki hame user assign karna h
            
            posts.user = request.user
            # request se hame current logged in user milta h
            # usko post ke user field me assign kar diya
            
            posts.save()
            # ab finally database me save kar diya
            
            return redirect('post_list')
            # save hone ke baad user ko post_list page par bhej diya

    else:
        # agar GET request h (user first time page open kare)
        # to empty form banayenge
        
        form = Postfrom()

    # chahe form empty ho ya invalid ho
    # hame template ko form bhejna hi h
    return render(request ,'post_form.html', {'form':form})

@login_required
def post_edit(request,post_id):
    # pehle post ko database se nikal rahe h
    # pk=post_id -> jis post ko edit karna h
    # user=request.user -> sirf wahi post mile jo current user ki ho
    post = get_object_or_404(Post, pk=post_id, user=request.user)

    if request.method == 'POST':
        # agar edit form submit hua h
        
        form = Postfrom(request.POST , request.FILES, instance=post)
        # instance=post ka matlab existing object ko update karna h
        # naya create nahi karna
        
        if form.is_valid():
            post = form.save(commit=False)
            # phir se commit=False kyuki user ensure karna h
            
            post.user = request.user
            # security ke liye fir se user assign
            
            post.save()
            # updated data database me save
            
            return redirect('post_list')
            # update hone ke baad list page par bhej diya

    else:
        # agar GET request h
        # to form me already existing data fill karke dikhayenge
        
        form = Postfrom(instance=post)

    return render(request ,'post_form.html', {'form':form})

@login_required
def post_delete(request,post_id):
    # jis post ko delete karna h use nikal rahe h
    # aur ensure kar rahe h ki wo current user ki hi ho
    post = get_object_or_404(Post, pk=post_id, user=request.user)

    if request.method == 'POST':
        # delete confirmation ke baad hi delete karenge
        
        post.delete()
        # database se permanently delete
        
        return redirect('post_list')
        # delete hone ke baad list page par bhej diya

    # agar GET request h to pehle confirmation page dikhayenge
    return render(request ,'post_delete_confirm.html', {'post':post})


def register(request):
    if request.method=='POST':
        form= UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('post_list')

    else:
        form=UserRegistrationForm()
    return render(request ,'registration/register.html', {'form':form})
 