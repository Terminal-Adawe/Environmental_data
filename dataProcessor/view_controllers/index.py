from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from analytics.models import modules

# Create your views here.

def index(request):
	if request.user.is_authenticated:
		queryset = modules.objects.filter(active=1,is_fillable=1)
		return render(request, 'dataProcessor/index.html', {'modules' : queryset})
	else:
		return HttpResponseRedirect('/analytics/login/')


