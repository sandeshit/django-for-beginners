from .models import BlogPost
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class BlogListView(ListView):
    model = BlogPost
    template_name = 'blogs_home.html'

# Create your views here.
class BlogDetailView(DetailView):
    model = BlogPost  
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    model = BlogPost
    template_name = 'post_new.html'
    fields = ['title','author','body']

class BlogUpdateView(UpdateView):
    model = BlogPost
    template_name = 'post_edit.html'
    fields = ['title','body']

class BlogDeleteView(DeleteView):
    model = BlogPost
    template_name = 'post_delete.html'
    success_url = reverse_lazy('blogs_home')
