from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('blog', views.blog, name='blog'),

    # email
    path('<int:post_id>/share/', views.post_share, name='post_share'),

]
