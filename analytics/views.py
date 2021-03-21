from django.shortcuts import render
from django.http import HttpResponse
from analytics.models import ComplianceValue
from analytics.models import Storage_facility
from analytics.models import Grease_and_hydocarbon_spillage

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def component_values(request):
	queryset = ComplianceValue.objects.all()
	return render(request, 'analytics/dashboard/component_values.html',{'data':queryset})

def reports(request):
	queryset = Storage_facility.objects.all().order_by('-created_at')[:4]
	queryset2 = Grease_and_hydocarbon_spillage.objects.all().order_by('-created_at')[:4]
	return render(request, 'analytics/dashboard/reports.html',{'data1':queryset,'data2':queryset2})

def view_report(request, module, report_id):
	reportid = report_id
	module = module

	queryset = Storage_facility.objects.filter(id=reportid).get()

	return render(request, 'analytics/dashboard/view_report.html',{'data':queryset})