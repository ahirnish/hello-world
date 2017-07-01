from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index( request ):
    return HttpResponse( "Hello, Ahirnish!" )

def index1( request ):
    return HttpResponse( "Hello, Axunna!" )
