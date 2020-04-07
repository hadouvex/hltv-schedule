from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls import url


from .api import MatchApi


urlpatterns = [
    path('api/matches', MatchApi.as_view()),
    path('matches', TemplateView.as_view(template_name='index.html'))
]
