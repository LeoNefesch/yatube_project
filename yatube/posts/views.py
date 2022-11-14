from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse('Welcome to Main page')

def group_posts(request, slug):
    return HttpResponse(f'Page about group {slug}')
