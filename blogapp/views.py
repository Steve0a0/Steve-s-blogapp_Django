from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect, render,get_object_or_404
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import profilepage
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
# Create your views here.

def homepage(request):
    q=request.GET.get('q')
    category = request.GET.get('category')
    
    category_query=Q()
    search_query=Q()
    
    if category:
        category_query = Q(categories__icontains=category)
    
    
    if q:
        multiple_q = Q(author__first_name__icontains=q) | Q(title__icontains=q) | Q(categories__icontains=q)
        post = NewPost.objects.filter(multiple_q)
    else:
        post= NewPost.objects.filter(category_query).order_by('-publication_time')
    query =category_query & search_query
    user=request.user
    context= {'user':user,'posts':post, 'search_query': q}
    return render (request,"home.html", context)

def articlepage(request,pk):
    post=get_object_or_404(NewPost, pk=pk)
    return render (request, "article.html", {'posts': post, 'user': request.user})

@csrf_protect
def addpost(request):
    if request.method =="POST":
        title=request.POST['title']
        content=request.POST['editor']
        author=request.POST['author']
        date=request.POST['date']
        categories=request.POST['categories']
        upload=request.FILES.get('image',None)
    
        author=request.user
        newpost=NewPost(title=title, content=content,author=author,publication_time=date,categories=categories,image=upload)
        newpost.save()
        return redirect('home')
        
    return render(request, "addpost.html")

@csrf_protect
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        print(username,pass1)
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "You have Entered the wrong Username or Password")
    
    return render(request, "login.html")

@csrf_protect
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        # Check if the passwords match before creating the user
        if pass1 == pass2:
            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = fname  
            myuser.last_name = lname    
            myuser.save()
            messages.success(request, "You have Successfully Signed up")
            return redirect("login")
        else:
            messages.error(request, "Passwords do not match")
    
    return render(request, "signup.html")

@csrf_protect
def logoutpage(request):       
    logout(request)
    return redirect('home')

@csrf_protect
def updatepost(request, pk):
    post = get_object_or_404(NewPost, pk=pk)
    
    if request.method == "POST":
        post.title = request.POST['title']
        post.content = request.POST['editor']
        post.author = request.user
        post.publication_time = request.POST['date']
        post.categories = request.POST['categories']
        
        if 'image' in request.FILES:
            post.image = request.FILES['image']
        
        post.save()
        return redirect('home')

    return render(request, 'update_page.html', {'user': request.user, 'posts': post})

def deletepost(request,pk):
    post=NewPost.objects.get(pk=pk)
    if request.method=="POST":
        post.delete()
        
        return redirect('home')
        
    return render (request,"delete_post.html" ,{'post': post})

@csrf_protect
def updateprofilepage(request):
    user_profile,created= profilepage.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST['fname']
        user.last_name = request.POST['lname']
        user.email = request.POST['email']
        user.save()
        
        user_profile.website = request.POST['website']
        user_profile.instagram = request.POST['instagram']
        user_profile.facebook = request.POST['facebook']
        user_profile.twitter = request.POST['twitter']
        if 'image' in request.FILES and request.FILES['image']:
            user_profile.profile_image = request.FILES['image']
        user_profile.contact = request.POST['Contact']
        user_profile.bio = request.POST['content']
        user_profile.save()
        
        messages.success(request, 'Profile updated successfully.')
        return redirect('profile')
    
    return render(request, 'updateprofile.html', {'user_profile': user_profile})

@login_required
def profilepagee(request):
    try:
        user_profile = profilepage.objects.get(user=request.user)
    except profilepage.DoesNotExist:
       
        user_profile = profilepage(user=request.user)
        user_profile.save()
    return render(request,'profile.html',{'user_profile':user_profile})


