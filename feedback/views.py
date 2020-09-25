from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.utils import timezone
from django.views import generic

from .forms import FeedbackForm
from .models import Feedback

class FeedbackView(generic.CreateView):
    form_class = FeedbackForm
    template_name = 'feedback/index.html'
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    # Handle POST GTTP requests
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/feedback/nice/')

        return render(request, self.template_name, {'form': form})