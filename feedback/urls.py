from django.urls import path
from . import views
from django.views.generic import TemplateView
from feedback.views import FeedbackView

app_name = 'feedback'
urlpatterns = [
    path('', FeedbackView.as_view(template_name = "feedback/index.html")), 
    path('nice/', TemplateView.as_view(template_name = "feedback/nice.html")),
]