from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from .forms import CommentForm, ContactForm
from django.views.generic import (CreateView, ListView, DetailView,
                                  DeleteView, UpdateView)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin)
from .models import Post, age_range, Contact
from django.contrib import messages
from .forms import CommentForm, ContactForm, AddPostForm                                



class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6

    # Function for age groups
    def get_context_data(self, *args, **kwargs):
        age_menu = age_range.objects.all()
        context = super(PostList, self).get_context_data(*args, **kwargs)
        context["age_menu"] = age_menu
        return context


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()    

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )




class PostLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)

        else: 
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug])) 



class AddPost(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Add post """
    model = Post
    template_name = 'add_post.html'
    form_class = AddPostForm
  



class UpdatePost(LoginRequiredMixin, UserPassesTestMixin,
                    SuccessMessageMixin, UpdateView):
    model = Post   
    template_name = 'update_post.html'
    form_class = AddPostForm
    success_message = "Post updated successfully"

    def test_func(self):
        """
        Check if the current user is the author of the post being updated
        """
        post = self.get_object()
        return self.request.user == post.author





def contact(request):
    """
    Submits contact us form to the admin dashboard only
    to be approved.
    """
    submitted = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thank_you.html?submitted = True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'contact.html',
                  {'form': form, 'submitted': submitted})     



def thank_you(request):
    template = 'thank_you.html'
    context = {}
    return render(request, template, context)

    
