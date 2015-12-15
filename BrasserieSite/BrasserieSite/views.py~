from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
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

def Commande(request):
    return render_to_response('Commande.html', {},RequestContext(request))

def contact(request):
    return render_to_response('contact.html', {},RequestContext(request))

def logout(request):
    return render_to_response('registration/logout.html', {},RequestContext(request))

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def Commande(request):
    return render(request, "Commande.html", {})


  
