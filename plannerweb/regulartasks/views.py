from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User

from . import models

# Create your views here.
def regular(request):
    rt = models.RegularTask.objects.all()
    context = {"tasks": rt, "RegularTask": models.RegularTask}
    return render(request, "regulartasks/regular.html", context=context)

def add(request):
    title = request.POST["title"]
    description = request.POST["description"]
    last_execution = request.POST["last_execution"]
    frequency_val = request.POST["frequency_val"]
    frequency_range = request.POST["frequency_range"]
    models.RegularTask.objects.create(title=title,
                                      description=description,
                                      last_execution=last_execution,
                                      frequency_range=frequency_range,
                                      frequency_val=frequency_val,
                                      user_id=User.objects.get(pk=2))

    return HttpResponseRedirect(reverse("regulartasks:regular"))