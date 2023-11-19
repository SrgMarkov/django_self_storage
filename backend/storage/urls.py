from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


app_name = 'storage'

urlpatterns = [
    path('', views.index, name='index'),
    path('boxes/', views.boxes, name='boxes'),
    path('faq/', views.faq, name='faq'),
    path('price/', views.price, name='price'),
    path('auth/', views.LoginUser.as_view(), name='auth'),
    path('registration/', views.RegisterUser.as_view(), name='registration'),
    path('forget/', views.RegisterUser.as_view(), name='forget'),
    path('logout/', views.logout_user, name='logout'),
    path('lk/', views.lk, name='lk'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

