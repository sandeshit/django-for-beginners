from .models import BlogPost
from django.views.generic import ListView, DetailView

class BlogListView(ListView):
    model = BlogPost
    template_name = 'blogs_home.html'

# Create your views here.
class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'post_detail.html'

