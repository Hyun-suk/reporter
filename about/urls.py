from django.urls import path
from django.views.generic import TemplateView

app_name='about'
urlpatterns = [
    path('service/', TemplateView.as_view(template_name = 'service.html'), name='service'),
]
