from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserCreationForm(forms.ModelForm):
    username = forms.CharField(label='إسم المستخدم', max_length=30, help_text='إسم المستخدم يجب ألا يحتوي على مسافات.')
    email = forms.EmailField(label='البريد الإلكتروني')
    first_name = forms.CharField(label='الإسم الأول')
    last_name = forms.CharField(label='الإسم الأخير')
    password1 = forms.CharField(label='كلمة المرور', widget=forms.PasswordInput(), min_length=8, help_text='كلمة المرور يجب ألا تقل عن 8 عناصر.')
    password2 = forms.CharField(label='تأكيد كلمة المرور', widget=forms.PasswordInput(), min_length=8)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('كلمة المرور غير مطابقة')
        return cd['password2']

    def clean_username(self):
        cd = self.cleaned_data
        if User.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError('يوجد مستخدم مسجل بهذا الإسم')
        return cd['username']

class LoginForm(forms.ModelForm):
    username = forms.CharField(label='إسم المستخدم')
    password = forms.CharField(label='كلمة المرور', widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'password']

class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(label='الإسم الأول')
    last_name = forms.CharField(label='الإسم الأخير')
    email = forms.EmailField(label='البريد الإلكتروني')
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
    
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']