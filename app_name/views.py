from django.views.generic import ListView, DetailView
from models import SimpleModel

class SimpleModelList(ListView):
    model = SimpleModel

class SimpleModelDetail(DetailView):
    model = SimpleModel