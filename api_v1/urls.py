from django.urls import path
from api_v1.views import PicView, AlbumView, get_csrf_token

app_name = 'api_v1'

urlpatterns = [
    path('get-token/', get_csrf_token, name='get_token'),
    path('picture/<int:pk>/', PicView.as_view(), name='pic_fav'),
    path('album/<int:pk>/', AlbumView.as_view(), name='album_fav'),
]
