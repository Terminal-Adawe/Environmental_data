import csv
import xlwt

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
from analytics.models import GeoReferencePoints
from analytics.models import FuelFarm
from analytics.models import WasteDetails
from analytics.models import WorkEnvCompliance
from analytics.models import Warehouse
from analytics.models import Conveyers
from analytics.models import IncidentReport
from analytics.models import modules
from analytics.models import Image
from analytics.view_controllers.sys_functions import get_model_using_modules
from analytics.view_controllers.sys_functions import get_fields_of_model
import logging

# Get an instance of a logger
logger = logging.getLogger("django")


def export_report(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			module = request.POST['module_name']

			report_format = ""

			if 'format' in request.POST:
				report_format = "xls"
			else:
				report_format = "csv"


			myModel = Storage_facility


			# Get field list of model
			myModel = get_model_using_modules(module)

			field_list = get_fields_of_model(myModel)
					

			logger.info("modules fields are ")
			# logger.info(modules._meta.get_fields())
			logger.info(field_list)

			fields = field_list
			columns = field_list


			# if module == "storage_facility":
			# 	myModel = Storage_facility
			# 	fields = ['Status of Seepage Point', 'Stability of Dam Walls', 'Holding Capacity', 'Current Capacity','Spillways Capacity','Spillways Stability','Signs of Erosion Spillway Tip','Comment','Report date']
			# 	columns = ['status_of_seepage_point','stability_of_dam_walls','holding_capacity','current_capacity','spillways_capacity','spillways_stability','signs_of_erosion_spillway_tip','comment','created_at']
		
			if 'from' in request.POST:
				from_date = request.POST['from']
			else:
				from_date = ''
			
			if 'to' in request.POST:
				to_date = request.POST['to']
			else:
				to_date = ''

			if report_format == "csv":
				response = HttpResponse(content_type='text/csv')
				response['Content-Disposition'] = 'attachment; filename="'+module+'.csv"'

				writer = csv.writer(response)

				writer.writerow(fields)
				
				if from_date == '' and to_date == '':
					if 'report_id' in request.POST:
						columns = myModel.objects.filter(id=request.POST['report_id']).values_list(*columns)
					else:
						columns = myModel.objects.all().values_list(*columns)
				elif from_date != '' and to_date == '':
					if 'report_id' in request.POST:
						columns = myModel.objects.filter(created_at__gte=from_date, id=request.POST['report_id']).values_list(*columns)
					else:
						columns = myModel.objects.filter(created_at__gte=from_date).values_list(*columns)
				elif from_date == '' and to_date != '':
					if 'report_id' in request.POST:
						columns = myModel.objects.filter(created_at__lte=to_date, id=request.POST['report_id']).values_list(*columns)
					else:
						columns = myModel.objects.filter(created_at__lte=to_date).values_list(*columns)
				else:
					if 'report_id' in request.POST:
						columns = myModel.objects.filter(created_at__gte=from_date,created_at__lte=to_date,id=request.POST['report_id']).values_list(*columns)
					else:
						columns = myModel.objects.filter(created_at__gte=from_date,created_at__lte=to_date).values_list(*columns)

				for column in columns:
					writer.writerow(column)

			if report_format == "xls":
				response = HttpResponse(content_type='application/ms-excel')
				response['Content-Disposition'] = 'attachment; filename="'+module+'.xls"'

				wb = xlwt.Workbook(encoding='utf-8')
				ws = wb.add_sheet('report_sheet')

				# Sheet header, first row
				row_num = 0

				font_style = xlwt.XFStyle()
				font_style.font.bold = True

				for col_num in range(len(fields)):
					ws.write(row_num, col_num, fields[col_num], font_style)

				# Sheet body, remaining rows
				font_style = xlwt.XFStyle()
				if from_date == '' and to_date == '':
					rows = myModel.objects.all().values_list(*columns)
				elif from_date != '' and to_date == '':
					rows = myModel.objects.filter(created_at__lte=to_date).values_list(*columns)
				elif from_date == '' and to_date != '':
					rows = myModel.objects.filter(created_at__gte=from_date).values_list(*columns)
				else:
					rows = myModel.objects.filter(created_at__gte=from_date,created_at__lte=to_date).values_list(*columns)

				# rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in rows ]

				for row in rows:
					row_num += 1

					for col_num in range(len(row)):
						if col_num.tzinfo and col_num.tzinfo is not None and col_num.tzinfo.utcoffset(col_num) is not None:
							ws.write(row_num, col_num, row[col_num].replace(tzinfo=None), font_style)
						else:
							ws.write(row_num, col_num, row[col_num], font_style)

				wb.save(response)

	return response
