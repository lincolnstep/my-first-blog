from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name="home"),
    path('myblog/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('about/',views.aboutme,name='about'),
    path('contactme/',views.contact_us,name='contact'),
    path('clear',views.clear,name='clear')

]
