from django.urls import path, re_path
from django.views.generic.base import RedirectView, TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='accueil.html'), name='accueil'),
    path('Apropos/', TemplateView.as_view(template_name='Apropos.html'), name='Apropos'),
    path('livres/', views.livres_liste, name='livres_liste'),
    path('livres/<int:livre_id>/', views.livre_detail, name='livre_detail'),
    path('livres/nouveau/', views.livre_nouveau, name='livre_nouveau'),
]


