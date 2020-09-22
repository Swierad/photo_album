from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .forms import UserCreateForm, UserLoginForm, PhotoFieldForm
from django.views.generic.edit import CreateView, FormView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import User, Photo


#Main Page
class PhotoAlbumView(View):
    def get(self, request):
        photos = Photo.objects.all()
        ctx = {'photos': photos}
        return render(request, "index.html", ctx)

    # form that allows to upload a photo
    def post(self, request):
        f = PhotoFieldForm(request.user, request.POST, request.FILES)
        if f.is_valid():
            f.save()
            return reverse_lazy("index.html")
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
                if user.is_active:
                    login(request, user)
                    return redirect(reverse('index'))
                else:
                    form.add_error(None, "Konto nie jest aktywne")
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
    template_name = "Auto_Zdam/user_create.html"
    success_url = reverse_lazy("index")