from django.urls import path
from blogs.views import*

urlpatterns = [
    path('', register, name='register'),
    path('login-page', login_page, name='login_page'),
    path('logout-page/',logout_page,name='logout_page'),

    path('home',home,name='home'),
    path('blog_list/',blog_list, name='blog_list'),
    path('add_blog/',add_blog, name='add_blog'),
    
    path('blog_detail/<str:b_id>/',blog_detail, name='blog_detail'),
    path('edit_blog/<str:b_id>/',edit_blog, name='edit_blog'),
    path('delete_blog/<str:b_id>/',delete_blog, name='delete_blog'),
    
]
