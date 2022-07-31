from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.URLShortenView.as_view()),
    path('thanks/', TemplateView.as_view(template_name='shortner/thanks.html')),
    path('sh/<int:code>', views.short_url, name='code'),
]