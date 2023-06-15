from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.db.transaction import atomic
from django.forms import CharField, Textarea, ModelForm, HiddenInput
from django.http import request
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.models import Profile


# Create your views here.


class SignUpForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    biography = CharField(label='My biography', widget=Textarea, min_length=40)

    @atomic
    def save(self, commit=True):
        self.instance.is_active = True
        result = super().save(commit)
        biography = self.cleaned_data['biography']
        profile = Profile(user=result, biography=biography)
        if commit:
            profile.save()
        return result


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'


class ProfileForm(ModelForm):

    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {'user': HiddenInput()}

    def clean_biography(self):
        cleaned_data = super().clean()
        biography = cleaned_data.get('biography').strip()
        if biography is None:
            raise ValidationError('Biography can not be empty.')
        if len(biography) < 40:
            raise ValidationError('Biography should have minimum 40 letters.')
        return biography


class ProfileCreateView(CreateView):
    template_name = 'new_profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('users')

    def get_initial(self):
        self.initial = {"user": self.request.user,
                        "biography": "Zde napiš něco o sobě"}
        return self.initial
