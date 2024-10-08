from django.shortcuts import reverse, redirect
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from rest_framework.exceptions import PermissionDenied
from webapp.forms import AlbumForm
from webapp.models import Album, Picture
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin


class AlbumDetailView(LoginRequiredMixin, DetailView):
    model = Album
    template_name = 'albums/album_detail.html'
    context_object_name = 'album'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        public_pictures = Picture.objects.filter(album=self.object, private=False).order_by('-created_date')
        paginator = Paginator(public_pictures, self.paginate_by)
        page_number = self.request.GET.get('page')
        context['public_pictures'] = paginator.get_page(page_number)
        return context


class AlbumCreateView(LoginRequiredMixin, CreateView):
    model = Album
    template_name = 'albums/album_create.html'
    form_class = AlbumForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:home')


class AlbumUpdateView(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'albums/album_update.html'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != request.user:
            raise PermissionDenied("You do not have permission to edit this.")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        album = form.save()
        pictures = Picture.objects.filter(album=album)
        if album.private:
            for picture in pictures:
                picture.private = True
                picture.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:album_detail', kwargs={'pk': self.object.pk})


class AlbumDeleteView(DeleteView):
    model = Album

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != request.user:
            raise PermissionDenied("You do not have permission to delete this.")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect("webapp:home")

    def delete(self, request, *args, **kwargs):
        album = self.get_object()
        pictures_to_delete = Picture.objects.filter(album=album)
        for picture in pictures_to_delete:
            picture.delete()
        return super().delete(request, *args, **kwargs)
