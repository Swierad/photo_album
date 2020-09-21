from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate, login, logout

class PhotoAlbumView(View):
    def get(self, request):
        return render(request, "index.html")

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