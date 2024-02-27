from django.urls import path
from .views import HomePageView, AboutPage, LandingPageView

app_name = 'home_app'
urlpatterns = [
    path("", HomePageView.as_view(), name='home'),
    path("landingpage", LandingPageView.as_view(), name='landing'),
    path("about/", AboutPage.as_view(), name='about'),
]