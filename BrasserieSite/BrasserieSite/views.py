from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
def index(request):
    return render_to_response('index.html', {},RequestContext(request))

def NosBiere(request):
    return render_to_response('NosBiere.html', {},RequestContext(request))


def BARBANE_DEMENTHE(request):
    return render_to_response('BARBANE_DEMENTHE.html', {},RequestContext(request))

def profile(request):
    return render_to_response('registration/profile.html', {},RequestContext(request))

def BARBANE_FLORALE(request):
    return render_to_response('BARBANE_FLORALE.html', {},RequestContext(request))

def BARBANE_BLONDE(request):
    return render_to_response('BARBANE_BLONDE.html', {},RequestContext(request))

def BARBANE_NOEL(request):
    return render_to_response('BARBANE_NOEL.html', {},RequestContext(request))

def BARBANE_MONDIALE(request):
    return render_to_response('BARBANE_MONDIALE.html', {},RequestContext(request))

def BARBANE_DANS_LES_VIGNES(request):
    return render_to_response('BARBANE_DANS_LES_VIGNES.html', {},RequestContext(request))

@login_required
def Commande(request):
    return render(request, "commande.html", {})
  
