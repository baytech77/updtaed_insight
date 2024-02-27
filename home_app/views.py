# from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Courses


# Create your views here.
# def home(request):
# return render(request, 'home/index.html')
class HomePageView( LoginRequiredMixin,ListView):
    model = Courses
    template_name = 'home/index.html'
    context_object_name = 'courses'


class LandingPageView(TemplateView):
    template_name = 'landingpage.html'



class AboutPage(TemplateView):
    template_name = 'about/about.html'