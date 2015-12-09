from django.shortcuts import render_to_response
from django.template import RequestContext
from .forms import ContactForm
from django.shortcuts import render

def index(request):
    return render_to_response('index.html', {},RequestContext(request))

def NosBiere(request):
    return render_to_response('NosBiere.html', {},RequestContext(request))


def contact(request):
    form_class = ContactForm
    
    return render(request, 'contact.html', {
        'form': form_class,
    })

