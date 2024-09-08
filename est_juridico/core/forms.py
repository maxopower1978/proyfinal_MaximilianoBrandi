from django.forms import UserChangeForm

class UserEditForm(UserChangeForm):
    password = None
    email = forms.EmailField(label = 'Ingrese su email:')
    last_name = forms.CharField(label = 'Apellido:')   
    first_name = forms.CharField(label = 'Nombre:')   

    class Meta:
        model = User
        fields = ['email','last_name','first_name']