from .models import User


class UserLoginForm(forms.Form):
    username = forms.CharField(label = 'Login')
    password = forms.CharField(label = 'Hasło', widget = forms.PasswordInput)


class UserCreateForm(forms.ModelForm):
    password2 = forms.CharField(label = 'Password (again)', widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password', 'password2', 'first_name', 'last_name', 'wherefrom']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):
        super().clean()
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']

        if password != password2:
            msg = 'Podane hasła są różne'
            self._errors['password2'] = self.error_class([msg])
            del self.cleaned_data['password2']

            '''
            Dla non-field error:
            from django.forms.forms import NON_FIELD_ERRORS
            form._errors[NON_FIELD_ERRORS] = form.error_class(['komunikat'])
            '''

        return self.cleaned_data