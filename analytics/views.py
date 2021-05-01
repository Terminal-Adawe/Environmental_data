import csv
from django.shortcuts import render
from django.http import HttpResponse
from analytics.models import ComplianceValue
from analytics.models import Storage_facility
from analytics.models import Grease_and_hydocarbon_spillage
from analytics.models import Waste_Management
from analytics.models import Inceneration
from analytics.models import Liquid_waste_oil
from analytics.models import Health_and_hygiene_awareness
from analytics.models import Energy_management
from analytics.models import Complaints_register
from analytics.models import Slope_stabilization_and_surface_water_retention
from analytics.models import Safety_training
from analytics.models import Safety_permission_system
from analytics.models import Safety_tools
from analytics.models import modules
from analytics.models import Image

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def component_values(request):
	queryset = ComplianceValue.objects.all()
	return render(request, 'analytics/dashboard/component_values.html',{'data':queryset})

def reports(request):
	queryset = Storage_facility.objects.all().order_by('-created_at')[:4]
	queryset2 = Grease_and_hydocarbon_spillage.objects.all().order_by('-created_at')[:4]
	queryset3 = Waste_Management.objects.all().order_by('-created_at')[:4]
	queryset4 = Inceneration.objects.all().order_by('-created_at')[:4]
	queryset5 = Liquid_waste_oil.objects.all().order_by('-created_at')[:4]
	queryset6 = Health_and_hygiene_awareness.objects.all().order_by('-created_at')[:4]
	queryset7 = Energy_management.objects.all().order_by('-created_at')[:4]
	queryset8 = Complaints_register.objects.all().order_by('-created_at')[:4]
	queryset9 = Slope_stabilization_and_surface_water_retention.objects.all().order_by('-created_at')[:4]
	queryset10 = Safety_training.objects.all().order_by('-created_at')[:4]
	queryset11 = Safety_permission_system.objects.all().order_by('-created_at')[:4]
	queryset12 = Safety_tools.objects.all().order_by('-created_at')[:4]

	queryset13 = modules.objects.all()

	return render(request, 'analytics/dashboard/reports.html',
		{'data1':queryset,
			'data2':queryset2,
			'data3':queryset3,
			'data4':queryset4,
			'data5':queryset5,
			'data6':queryset6,
			'data7':queryset7,
			'data8':queryset8,
			'data9':queryset9,
			'data10':queryset10,
			'data11':queryset11,
			'data12':queryset12,
			'modules':queryset13})

def view_report(request, module, report_id):
	reportid = report_id
	module = module

	myModel = Storage_facility

	if module == "storage_facility":
		myModel = Storage_facility
	elif module == "Grease_and_hydocarbon":
		myModel = Grease_and_hydocarbon_spillage
	elif module == "Waste_Management":
		myModel = Waste_Management
	elif module == "Inceneration":
		myModel = Inceneration
	elif module == "liquid_waste_and_oil":
		myModel = Liquid_waste_oil
	elif module == "health_and_hygiene_awareness":
		myModel = Health_and_hygiene_awareness
	elif module == "energy_management":
		myModel = Energy_management
	elif module == "complaints_register":
		myModel = Complaints_register
	elif module == "slope_stabilization":
		myModel = Slope_stabilization_and_surface_water_retention
	elif module == "safety_permission_system":
		myModel = Safety_permission_system
	elif module == "safety_training":
		myModel = Safety_training
	elif module == "safety_tools":
		myModel = Safety_tools


	queryset = myModel.objects.filter(id=reportid).get()

	modules_queryset = modules.objects.filter(module_name=module)
	image_queryset = Image.objects.filter(report_id=reportid, module_id__in=modules_queryset.values('id'))

	return render(request, 'analytics/dashboard/view_report.html',{'data':queryset,'module':module,'images':image_queryset})

def view_all_reports(request, module):
	module = module

	myModel = Storage_facility

	if module == "storage_facility":
		myModel = Storage_facility
	elif module == "Grease_and_hydocarbon":
		myModel = Grease_and_hydocarbon_spillage
	elif module == "Waste_Management":
		myModel = Waste_Management
	elif module == "Inceneration":
		myModel = Inceneration
	elif module == "liquid_waste_and_oil":
		myModel = Liquid_waste_oil
	elif module == "health_and_hygiene_awareness":
		myModel = Health_and_hygiene_awareness
	elif module == "energy_management":
		myModel = Energy_management
	elif module == "complaints_register":
		myModel = Complaints_register
	elif module == "slope_stabilization":
		myModel = Slope_stabilization_and_surface_water_retention
	elif module == "safety_permission_system":
		myModel = Safety_permission_system
	elif module == "safety_training":
		myModel = Safety_training
	elif module == "safety_tools":
		myModel = Safety_tools

	queryset13 = modules.objects.all()

	queryset = myModel.objects.all()

	return render(request, 'analytics/dashboard/reports_all_records.html',{'data':queryset,'module':module, 'modules':queryset13})


