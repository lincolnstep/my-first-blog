from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post,Project,Aboutme,Quote
from django.contrib import messages
from django.core.mail import send_mail

from vivekv.settings import EMAIL_HOST_USER
from blog.forms import ContactForm

def home(request):
    twoposts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    recentposts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    mybio= Aboutme.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    myquote=Quote.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/home.html', {'twoposts':twoposts, 'recentposts':recentposts, 'mybio' : mybio , 'myquote' : myquote})


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    recentposts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

    return render(request, 'blog/myblog.html', {'posts': posts, 'recentposts':recentposts, })


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def aboutme(request):
    projects = Project.objects.order_by('-startdate')
    mybio= Aboutme.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/aboutme.html', {'projects':projects, 'mybio' : mybio ,})


def send_email(contact_form_data):
    email_message_format = 'name: %s\nemail: %s\nMessage: %s\n'
    name = contact_form_data.get('name', '')
    message = contact_form_data.get('message', '')
    email = contact_form_data.get('email')
    email_message_format = email_message_format % (name, email, message)
    send_mail("Vivekanand/'s Blog", email_message_format, EMAIL_HOST_USER, [EMAIL_HOST_USER], fail_silently=False,)

def contact_us(request):
    try:
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                send_email(form.cleaned_data)
                messages.success(request, 'Your response has been recorded')
        else:
            form = ContactForm()
    except:
        messages.error(request, 'Please configure your email settings.')

    return render(request, 'blog/contact.html', {'page':'contact', 'form':form})

def clear(request):
    form = ContactForm()
    messages.error(request, 'Fields cleared successfully')
    return render(request, 'blog/contact.html', {'page':'contact', 'form':form})
