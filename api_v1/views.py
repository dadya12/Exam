from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from webapp.models import Picture, Album
from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def get_csrf_token(request):
    if request.method == 'GET':
        return HttpResponse()
    else:
        return HttpResponseNotAllowed(permitted_methods=["GET"])


class PicView(APIView):

    def get(self, request, *args, pk, **kwargs):
        pic = get_object_or_404(Picture, pk=pk)
        if request.user in pic.favorite.all():
            pic.favorite.remove(request.user)
            fav = False
        else:
            pic.favorite.add(request.user)
            fav = True
        return JsonResponse({'favorite': fav})


class AlbumView(APIView):
    def get(self, request, *args, pk, **kwargs):
        album = get_object_or_404(Album, pk=pk)
        if request.user in album.favorite.all():
            album.favorite.remove(request.user)
            fav = False
        else:
            album.favorite.add(request.user)
            fav = True
        return JsonResponse({'favorite': fav})
