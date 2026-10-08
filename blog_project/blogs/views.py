from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from blogs.models import*

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        conf_password = request.POST.get('conf_password')
        
        user_exist = UserModel.objects.filter(username = username).exists()
        if user_exist:
            messages.warning(request, 'User already exists')
            return redirect('register')
        
        if password == conf_password:
            UserModel.objects.create_user(
                username = username,
                full_name = full_name,
                email = email,
                password= password,
            )
            messages.success(request, 'User created successfully')
            return redirect('login_page')
        else:
            messages.warning(request, 'Password doesnot match.')
            return redirect('register')

    return render(request, 'auth/register.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username = username, password = password)
        if user:
            login(request, user)
            messages.success(request, 'User login successfully')
            return redirect('home')
        else:
            messages.warning(request, 'Invalid credentials.')
            return redirect('login_page')

    return render(request, 'auth/login.html')

@login_required
def logout_page(request):
    logout(request)
    return redirect('login_page')


@login_required
def home(request):
    
    blogs = BlogModel.objects.all().order_by('-publish_date')

    context = {
        'blogs': blogs
    }
    return render(request, 'pages/home.html', context)

@login_required
def blog_list(request):

    blogs = BlogModel.objects.all().order_by('-publish_date')
    search = request.GET.get('search', '')
    if search:
        blogs = blogs.filter(
            title__icontains=search
        ) | blogs.filter(
            author_name__icontains=search
        )

    context = {
        'blogs': blogs,
        'search': search,
    }
    return render(request, 'pages/blog_list.html', context)

@login_required
def blog_detail(request, b_id):

    blog = get_object_or_404(BlogModel,id = b_id)

    context = {
        'blog': blog
    }
    return render(request,'pages/blog_detail.html',context)

@login_required
def add_blog(request):
    
    if request.method == 'POST':
        title = request.POST.get('title')
        author_name = request.POST.get('author_name')
        content = request.POST.get('content')
        category = request.POST.get('category')
        blog_image = request.FILES.get('blog_image')
        
        BlogModel.objects.create(
            title = title,
            author_name = author_name,
            content = content,
            category = category,
            blog_image = blog_image,
        ) 
        
        return redirect('blog_list')
    return render(request, 'pages/add_blog.html')


@login_required
def edit_blog(request, b_id):

    blog_data = BlogModel.objects.get(id=b_id)
    if request.method == 'POST':

        title = request.POST.get('title')
        author_name = request.POST.get('author_name')
        content = request.POST.get('content')
        category = request.POST.get('category')
        publish_date = request.POST.get('publish_date')
        blog_image = request.FILES.get('blog_image')

        blog_data.title = title
        blog_data.author_name = author_name
        blog_data.content = content
        blog_data.category = category
        
        if publish_date:
            blog_data.publish_date = publish_date

        if blog_image:
            blog_data.blog_image = blog_image
            
        blog_data.save()

        return redirect('blog_list')

    context = {
        'blog_data': blog_data
    }
    return render(request,'pages/edit_blog.html',context)
    
@login_required
def delete_blog(request, b_id):
    BlogModel.objects.get(id=b_id).delete()
    return redirect('blog_list')
