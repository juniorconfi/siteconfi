from django.shortcuts import render
# Create your views here.


def index(request):
	context = {}
	template = 'pagina-inicial.html'
	return render(request,template,context)

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
print BASE_DIR
STATIC_ROOT = 'C:\sistemasconfi\heroku\venv\src\static'
print STATIC_ROOT