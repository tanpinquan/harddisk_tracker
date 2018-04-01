from django.shortcuts import render

# Create your views here.
from .models import Hdd
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Hdd
import datetime
    
def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_hdds=Hdd.objects.all().count()
    # Available books (status = 'a')
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_hdds':num_hdds},
    )


class HddListView(generic.ListView):
    model = Hdd
    template_name = 'index.html'  # Specify your own template name/location
    
    
    
class HddCreate(CreateView):
    model = Hdd
    fields = '__all__'
    success_url = reverse_lazy('index')
    
#    template_name = 'hdd_form.html'  # Specify your own template name/location

    
class HddUpdate(UpdateView):
    model = Hdd
    fields = ['borrower','date']
    initial={'date':datetime.date.today()}
    success_url = reverse_lazy('index')
