from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

def function(request):
    return render(request, 'second_task/function_based_template.html')

class ClassBV(TemplateView):
    template_name = 'second_task/class_based_template.html'