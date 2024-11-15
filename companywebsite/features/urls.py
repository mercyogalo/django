from django.urls import path
from . import views


urlpatterns = [
     path('',views.index, name="home"),
    path('about/',views.about,name="about"),
    path('blogDetails/',views.blogDetails,name='blogDetails'),
    path('blog/',views.blog,name="blog"),
    path('contact/',views.contact,name="contact"),
    path('portfolioDetails/',views.portfolioDetails,name="portfolioDetails"),
    path('portfolio/',views.portfolio,name="portfolio"),
    path('pricing/',views.pricing,name="pricing"),
    path('serviceDetails/',views.serviceDetails,name="serviceDetails"),
    path('services/',views.services,name="services"),
    path('team/',views.team,name="team"),
    path('testimonials/',views.testimonials,name="testimonials"),
]