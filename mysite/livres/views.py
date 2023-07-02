from django.shortcuts import render, get_object_or_404, redirect
from .models import Livre

def livre_detail(request, livre_id):
    livre = get_object_or_404(Livre, pk=livre_id)
    return render(request, 'livres/livre_detail.html', {'livre': livre})

def livres_liste(request):
    livres = Livre.objects.all()
    return render(request, 'livres/livres_liste.html', {'livres': livres})

from .forms import LivreForm

def livre_nouveau(request):
    if request.method == "POST":
        form = LivreForm(request.POST, request.FILES)
        if form.is_valid():
            livre = form.save()
            return redirect('livre_detail', livre_id=livre.id)
    else:
        form = LivreForm()
    return render(request, 'livres/livre_nouveau.html', {'form': form})




