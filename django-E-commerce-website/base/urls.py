from django.contrib import admin
from django.urls import path ,include, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('',views.home,name='home'),
    path('iteme_proile_<str:pk>',views.item_pro,name='item_pro'),
    path('sing in',views.saign_in,name='sing_in'),
    path('delet<str:pk>',views.delet,name='delet'),
    path('deal_<str:pk>',views.deal,name='deal'),
    path('login',views.loginn,name='login'),
    path('about',views.about,name='about')
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
