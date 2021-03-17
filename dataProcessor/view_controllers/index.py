from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
	if request.user.is_authenticated:
		print(request.user)
		return render(request, 'dataProcessor/index.html')
	else:
		return HttpResponseRedirect('/analytics/login/')


