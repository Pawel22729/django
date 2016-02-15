from django.views import generic
from django.shortcuts import render_to_response,RequestContext
from django.http import HttpResponseRedirect
from .models import Osoba, Wpisy
from .forms import WpisyForm

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


class PokazWpisy(generic.ListView):
	template_name = "pawel/wpisy.html"
	context_object_name = "wpisy"

	def get_queryset(self):
		wszystkie_wpisy = Wpisy.objects.all().order_by('-data_wpisu')[:3]
		return wszystkie_wpisy

def forma(request):
    if request.method == 'POST':
        form = WpisyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/wpisy/')
    else:
        form = WpisyForm()

    return render_to_response('pawel/dodaj_wpis.html', {'form': form}, RequestContext(request))

def test(request):
    if request.method == 'GET':
        data = request.GET.get('name')
    return render_to_response('pawel/test.html', {'data': data}, RequestContext(request))