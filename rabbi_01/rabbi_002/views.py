from django.http import HttpResponse
from django.shortcuts import render
from . forms import teacher_registration

# Create your views here.


def rabbi_0002(request):
    return render(request, "rabbi_002/rabbi_002.html")


def show_forms_data(request):
    fm = teacher_registration()
    #fm.order_fields(field_order=['email','last_name','first_name'])
    return render(request, 'rabbi_002/forms.html', {'forms':fm})
