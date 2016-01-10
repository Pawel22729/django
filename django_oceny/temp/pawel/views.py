from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Osoba
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'pawel/index.html'
    context_object_name = 'wszyscy_uczniowie'

    def get_queryset(self):
	osoby = Osoba.objects.all()
	osoby_oceny = {}
	for os in osoby:
	    oc_os = []
	    oceny = os.oceny_set.get_queryset()
	    for oc in oceny:
		oc_os.append(str(oc.nazwa_przedm)+' : '+str(oc.ocena_choice))
	    osoby_oceny[os] = oc_os
        return osoby_oceny
