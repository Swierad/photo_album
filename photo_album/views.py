from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .forms import UserCreateForm, UserLoginForm, PhotoForm, CommentForm
from django.views.generic.edit import CreateView, FormView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import User, Photo
from django.views.generic.edit import CreateView



#Main Page
class PhotoAlbumView(View):
    def get(self, request):
        photos = Photo.objects.all().order_by('creation_date')
        form = PhotoForm(initial={'user': request.user})
        ctx = {'photos': photos,
               'form': form}
        return render(request, "index.html", ctx)

    def post(self, request):
        f = PhotoForm(request.POST, request.FILES)
        photos = Photo.objects.all().order_by('creation_date')
        form = PhotoForm()
        ctx = {'photos': photos,
               'form': form}
        if f.is_valid():
            f.save()


            return render(request, "index.html", ctx)
                #reverse_lazy("index")
        print(f.errors)
        return render(request, "index.html", ctx)




class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, "user_login.html", {'form': form})

    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('index'))

            else:
                # user is None
                form.add_error(None, "Nieprawidłowy login lub hasło")
        return render(request, "user_login.html", {'form': form})


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('main'))

class UserCreateView(CreateView):
    form_class = UserCreateForm
    template_name = "user_create.html"
    success_url = reverse_lazy("index")

class CommentCreateView(CreateView):
    form_class = CommentForm
    template_name = "comment_create.html"
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        form.instance.photo_id = self.kwargs['pk']
        return super().form_valid(form)