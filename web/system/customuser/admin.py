from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from system.customuser.models import CustomUser

class UserCreationForm(forms.ModelForm):
    
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('email', 'username')

    def clean_password2(self):

        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1!=password2:
            raise forms.ValidationError("Passwords dont't match")
        return password2
    def save(self, commit=True):
        
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
   
    password = ReadOnlyPasswordHashField()

    class Meta:
        models = CustomUser
        fields = ['email', 'password', 'username', 'is_active', 'is_staff']

    def clean_password(self):
        return self.initial['password']

class CustomUserAdmin(UserAdmin):
    
    form = UserChangeForm
    add_form = UserCreationForm
    
    list_display = ('email', 'username', 'is_staff', 'is_active') 
    list_filter = ('is_staff',)      
    fieldsets = (
        (None, {'fields':('email', 'password')}),
        ('Permissions',{'fields':('is_staff', 'is_active')}),
    ) 
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.unregister(Group)
