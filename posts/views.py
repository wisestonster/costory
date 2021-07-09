from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
# from django.views import View
from django.views.generic import (
    CreateView, ListView, DetailView, UpdateView, DeleteView, RedirectView
)
from django.urls import reverse
from .models import Post
from .forms import PostForm


# Create your views here.
# def post_list(request):
#     posts = Post.objects.all()
#     paginator = Paginator(posts, 6)
#     curr_page_number = request.GET.get('page')
#     if curr_page_number is None:
#         curr_page_number = 1
#     page = paginator.page(curr_page_number)
#     return render(request, 'posts/post_list.html', {'page': page})

class PostListView(ListView):
    model = Post                            # 기본값이 없고 매번 지정해야 함
    # template_name = 'posts/post_list.html'  # 모델명_list
    context_object_name = 'posts'           # 오브젝트명_list
    ordering = ['-dt_created']
    paginate_by = 6
    # page_kwarg = 'page'                     # 기본값이 page 임

# def post_detail(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     context = {"post": post}
#     return render(request, 'posts/post_detail.html', context)

class PostDetailView(DetailView):
    model = Post
    # template_name='posts/post_detail.html'  # 기본값 모델명_detail.html
    # pk_url_kwarg = 'post_id'                    # 기본값 pk
    # context_object_name = 'post'                # 오브젝트명


# def post_create(request):
#     if request.method == 'POST':
#         post_form = PostForm(request.POST)
#         if post_form.is_valid():
#             new_post = post_form.save()
#             return redirect('post-detail', post_id=new_post.id)
#     else:
#         post_form = PostForm()
#     return render(request, 'posts/post_form.html', {'form': post_form})

# class PostCreateView(View):
#     def get(self, request):
#         post_form = PostForm()
#         return render(request, 'posts/post_form.html', {'form': post_form})
#     def post(self, request):
#         post_form = PostForm(request.POST)
#         if post_form.is_valid():
#             new_post = post_form.save()
#             return redirect('post-detail', post_id=new_post.id)

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    # template_name = 'posts/post_form.html'      # 기본값 오브젝트명_form.html

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.id})

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    # template_name = 'posts/post_form.html'
    # pk_url_kwarg = 'post_id'

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.id})

# def post_update(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     if request.method == 'POST':
#         post_form = PostForm(request.POST, instance=post) # 작성된 데이터와 Form을 바인딩
#         if post_form.is_valid():
#             post_form.save()
#             return redirect('post-detail', post_id=post.id)
#     else:  # GET 방식일 때
#         post_form = PostForm(instance=post)
#     return render(request, 'posts/post_form.html', {'form': post_form})

class PostDeleteView(DeleteView):
    model = Post
    # template_name = 'posts/post_confirm_delete.html'
    # pk_url_kwarg = 'post_id'
    # context_object_name = 'post'

    def get_success_url(self):
        return reverse('post-list')

# def post_delete(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     if request.method == 'POST':
#         post.delete()
#         return redirect('post-list')
#     else:
#         return render(request, 'posts/post_confirm_delete.html', {'post': post})

class IndexRedirectView(RedirectView):
    pattern_name = 'post-list'

# def index(request):
#     return redirect('post-list')