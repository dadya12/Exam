from django.contrib.auth import login, get_user_model
from django.shortcuts import redirect, reverse
from django.views.generic import CreateView, DetailView
from accounts.forms import MyUserCreationForm


class RegistrationView(CreateView):
    model = get_user_model()
    form_class = MyUserCreationForm
    template_name = 'create_user.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_page = self.request.GET.get('next')
        if not next_page:
            next_page = self.request.POST.get('next')
        if not next_page:
            next_page = reverse('webapp:home')
        return next_page


class UserDetailView(DetailView):
    template_name = 'user_detail.html'
    model = get_user_model()
    context_object_name = 'user_obj'
