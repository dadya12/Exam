from django.shortcuts import reverse, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework.exceptions import PermissionDenied

from webapp.forms import PictureForm
from django.contrib.auth.mixins import LoginRequiredMixin

from webapp.models import Picture


class PictureListView(ListView):
    model = Picture
    context_object_name = 'pictures'
    template_name = 'home.html'
    paginate_by = 3

    def get_queryset(self):
        return Picture.objects.filter(private=False).order_by('-created_date')


class PictureDetailView(DetailView):
    model = Picture
    template_name = 'pictures/picture_detail.html'


class PictureCreateView(LoginRequiredMixin, CreateView):
    model = Picture
    form_class = PictureForm
    template_name = 'pictures/picture_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['album'].queryset = form.fields['album'].queryset.filter(author=self.request.user)
        return form

    def get_success_url(self):
        return reverse('webapp:home')


class PictureUpdateView(UpdateView):
    model = Picture
    form_class = PictureForm
    template_name = 'pictures/picture_update.html'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != request.user:
            raise PermissionDenied("You do not have permission to edit this.")
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:picture_detail', kwargs={'pk': self.object.pk})


class PictureDeleteView(DeleteView):
    queryset = Picture.objects.all()

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != request.user:
            raise PermissionDenied("You do not have permission to delete this.")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect("webapp:home")
