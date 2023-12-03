from django.shortcuts import render

# Create your views here.
def regular(request):
    return render(request, "regulartasks/regular.html")