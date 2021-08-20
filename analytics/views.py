from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from rest_framework import viewsets
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
from analytics.models import Notifications
from analytics.models import NotificationViewer
from analytics.models import WasteDetails
from analytics.models import GeoReferencePoints
from analytics.models import FuelFarm
from analytics.models import WorkEnvCompliance
from analytics.models import Warehouse
from analytics.models import Conveyers
from analytics.models import IncidentReport
from analytics.models import Water_management
from analytics.models import modules
from analytics.models import Image
from analytics.models import Tasks
from analytics.models import Custom_table
from analytics.models import Graph_config
from analytics.models import reports
from analytics.serializers import TasksSerializer
from analytics.serializers import graphConfigSerializer
from analytics.serializers import UsernameSerializer
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from drf_multiple_model.views import ObjectMultipleModelAPIView
from rest_framework.response import Response
from rest_framework import status
import json
import logging
import sys

from analytics.view_controllers.notifications import insert_view_notification


# Get an instance of a logger
logger = logging.getLogger("django")

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def component_values(request):
	queryset = ComplianceValue.objects.all()
	return render(request, 'analytics/dashboard/component_values.html',{'data':queryset})

def reports_f(request):
	queryset = reports.objects.all()

	querysetm = modules.objects.filter(active=1)

	return render(request, 'analytics/dashboard/reports.html',
		{
			'data':queryset,
			'modules':querysetm})

def graphs(request):
	return render(request, 'analytics/dashboard/graphs.html')

def tables(request):
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
	queryset13 = GeoReferencePoints.objects.all().order_by('-created_at')[:4]
	queryset14 = FuelFarm.objects.all().order_by('-created_at')[:4]
	queryset15 = WorkEnvCompliance.objects.all().order_by('-created_at')[:4]
	queryset16 = Warehouse.objects.all().order_by('-created_at')[:4]
	queryset17 = Conveyers.objects.all().order_by('-created_at')[:4]
	queryset18 = IncidentReport.objects.all().order_by('-created_at')[:4]
	queryset19 = Water_management.objects.all().order_by('-created_at')[:4]

	custom_tables = Custom_table.objects.filter(active=1)

	querysetm = modules.objects.filter(active=1)

	return render(request, 'analytics/dashboard/tables.html',
		{
			'custom_tables':custom_tables,
			'data1':queryset,
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
			'data13':queryset13,
			'data14':queryset14,
			'data15':queryset15,
			'data16':queryset16,
			'data17':queryset17,
			'data18':queryset18,
			'data19':queryset19,
			'modules':querysetm})

def str_to_class(str):
    return getattr(sys.modules[__name__], str)

def view_table(request, module, report_id):
	if request.user.is_authenticated:
		user = request.user
		reportid = report_id
		module = module
		modules_queryset = modules.objects.filter(active=1)
		
		url = 'analytics/dashboard/view_table.html'
	
		# queryset = modules.objects.filter(id=module)
		# module = queryset[0].module_name
		if module=="custom":
			queryset = reportid
			url = 'analytics/dashboard/custom_table_view.html'
			module = 0
		else:
			myModel = Storage_facility
		
			for module_i in modules_queryset.values():
				if int(module) == module_i['id']:
					myModel = str_to_class(module_i['table'])
					logger.info(" Matches!! ")
					logger.info(module_i['table'])
		
			
		
			queryset = myModel.objects.filter(report_name=reportid)
		
			logger.info("Queryset is ")
			logger.info(queryset)
			# logger.info("And report ID is ")
			# logger.info(reportid)
	
			# try:
			insert_view_notification(user,reportid,module)
			# except:
			# 	logger.info("No notification sent ")

		modules_queryset_single = modules.objects.filter(id=module)
		image_queryset = Image.objects.filter(report_id=reportid, module_id__in=modules_queryset_single.values('id'))
	
		return render(request, url,{'report_data':queryset,'module':int(module),'modules':modules_queryset,'images':image_queryset})
	else:
		return HttpResponseRedirect('login')

def view_report(request, report_id):
	if request.user.is_authenticated:
		user = request.user
		reportid = report_id

		modules_queryset = modules.objects.filter(active=1)
		
		url = 'analytics/dashboard/view_report.html'
	
		return render(request, url,{'report_id':reportid,'modules':modules_queryset})
	else:
		return HttpResponseRedirect('login')

def view_all_reports(request, module):
	module = module

	modules_queryset = modules.objects.filter(active=1)

	myModel =  Custom_table
	url = 'analytics/dashboard/custom_tables_all.html'

	for module_i in modules_queryset.values():
			if module == module_i['module_name']:
				myModel = str_to_class(module_i['table'])
				url = 'analytics/dashboard/reports_all_records.html'

	queryset13 = modules.objects.filter(active=1)

	queryset = myModel.objects.filter(active=1)

	return render(request, url,{'data':queryset,'module':module, 'modules':queryset13})

def add_task(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			user = request.user

			task_for = request.user.username

			if request.POST['task_for']!="self":
				task_for = User.objects.get(username=request.POST['task_for'])
				task_for = task_for.username


			task_save = Tasks(
				task=request.POST['task'],
				description=request.POST['description'],
				start_time=request.POST['start_time'],
				end_time=request.POST['end_time'],
				created_by=user,
				task_for=task_for
			)
			task_save.save()
			return redirect(request.META['HTTP_REFERER'])
		else:
			return redirect(request.META['HTTP_REFERER'])
	else:
		return HttpResponseRedirect('login')

class Update_graph(viewsets.ViewSet):
	def create(self, request):
		serializer = graphConfigSerializer(data=request.data)

		if serializer.is_valid(raise_exception=True):
			graph_config = Graph_config.objects.get(id=int(serializer.data['id']))
			on_dashboard = True
			if serializer.data['value'] == 'true':
				on_dashboard=True
			else:
				on_dashboard=False

			graph_config.on_dashboard = on_dashboard
			graph_config.save()
	
			return Response("updated",status=status.HTTP_202_ACCEPTED)
		else:
			return Response(status=status.HTTP_400_BAD_REQUEST)



class GetUsers(ObjectMultipleModelAPIView):
	querylist=[
			{'queryset': User.objects.filter(is_active=1), 'serializer_class': UsernameSerializer},
	]

class Add_task(viewsets.ViewSet):
	def create(self, request):
		serializer = TasksSerializer(data=request.data)

		# user = User.objects.get(username=serializer.data['username'])
		# created_by_id = user.id