from django.contrib.auth.forms import UserChangeForm
from django.views import generic
from django.urls import reverse_lazy
from members.forms import SignUpForm, EditProfileForm


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UpdateProfileView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('all_files')

    def get_object(self, queryset=None):
        return self.request.user

