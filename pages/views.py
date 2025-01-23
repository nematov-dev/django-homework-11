from typing import Any
from django.shortcuts import render,redirect
from django.contrib import messages
from django.views.generic import TemplateView

from . import forms
from pages import models

def main_page_view(request):
    return render(request,'index.html')

def home_page_view(request):

    if request.path == '/en/home/' or '/uz/home/':
        header_type = 'home_header'
    else:
        header_type = 'default_header'
    
    return render(request, 'pages/home.html', {'header_type': header_type})



class AboutView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["posts"] = models.AboutModel.objects.all()
        return context




def contact_page_view(request):

    if request.method == "POST":
        
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your message save database')
            return redirect('pages:contact')

        else:
            messages.error(request,'Error')
            return redirect('pages:contact')

    else:
        return render(request,'pages/contact.html')