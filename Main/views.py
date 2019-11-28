import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth
from PostApp.models import Posts
from django.views.generic import TemplateView

class MainView(TemplateView):

    def get(self, request):
        ctx = {}
        if request.user.is_authenticated:
            contex = Posts.objects.all()
            ctx['contex'] = contex
        return render(request, 'main/main.html', ctx)