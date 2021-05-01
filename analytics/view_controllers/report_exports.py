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
from analytics.models import modules
from analytics.models import Image

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
			fields = []


			if module == "storage_facility":
				myModel = Storage_facility
				fields = ['Status of Seepage Point', 'Stability of Dam Walls', 'Holding Capacity', 'Current Capacity','Spillways Capacity','Spillways Stability','Signs of Erosion Spillway Tip','Comment','Report date']
				columns = ['status_of_seepage_point','stability_of_dam_walls','holding_capacity','current_capacity','spillways_capacity','spillways_stability','signs_of_erosion_spillway_tip','comment','created_at']
			elif module == "Grease_and_hydocarbon":
				myModel = Grease_and_hydocarbon_spillage
				fields = ['Storage Condition', 'Comment','Report Date']
				columns = ['storage_condition','comment','created_at']
			elif module == "Waste_Management":
				myModel = Waste_Management
				fields = ['Segregation at Source and Bins', 'Glass Waste Source', 'Glass Waste Weight', 'Plastic Waste Source','Plastic Waste Weight','Metal Waste Source','Metal Waste Weight','Comment','Report date']
				columns = ['segregation_at_source_and_bins','glass_waste_source','glass_waste_weight','plastic_waste_source','plastic_waste_weight','metal_waste_source','metal_waste_weight','comment','created_at']
			elif module == "Inceneration":
				myModel = Inceneration
				fields = ['Items Incenerated', 'Quantity', 'Temperature', 'Comment','Report Date']
				columns = ['items_incenerated','quantity','temperature','comment','created_at']
			elif module == "liquid_waste_and_oil":
				myModel = Liquid_waste_oil
				fields = ['Discharge Point', 'Source', 'Comment', 'Report Date']
				columns = ['discharge_point','source','comment','created_at']
			elif module == "health_and_hygiene_awareness":
				myModel = Health_and_hygiene_awareness
				fields = ['Training', 'Number of Staff', 'Number of Visitors', 'Training Duration', 'Comment', 'Report Date']
				columns = ['training','no_of_staff','no_of_visitors','duration','created_at']
			elif module == "energy_management":
				myModel = Energy_management
				fields = ['Total Energy Avialable', 'Camp Consumption', 'Admin Consumption', 'Workshop Consumption', 'Mine plant Consumption', 'Other Consumption', 'Comment', 'Report Date']
				columns = ['total_energy_available','camp_consumption','admin_consumption','workshop_consumption','mine_plant_consumption','other_consumption','comment','created_at']
			elif module == "complaints_register":
				myModel = Complaints_register
				fields = ['Number of Complaints', 'Status of Complaints', 'Comment', 'Report Date']
				columns = ['no_of_complaints','status_of_complaints','comment','created_at']
			elif module == "slope_stabilization":
				myModel = Slope_stabilization_and_surface_water_retention
				fields = ['Number of Exposed Unstabilized Slopes', 'Status', 'Comment', 'Report Date']
				columns = ['no_of_exposed_unstabilized_slopes','status','comment', 'created_at']
			elif module == "safety_training":
				myModel = Safety_training
				fields = ['Training', 'Number of Staff', 'Number of Inductions', 'Number of Visitors', 'Duration', 'Comment', 'Report Date']
				columns = ['training','no_of_staff','no_of_inductions','no_of_visitors','duration','created_at']
			elif module == "safety_permission_system":
				myModel = Safety_permission_system
				fields = ['Number of Permits Issued', 'Status', 'Comment', 'Report Date']
				columns = ['no_of_permits_issued','status','comment','created_at']
			elif module == "safety_tools":
				myModel = Safety_tools
				fields = ['Number of Estinguishers', 'Fire Alarm', 'Status of Estinguishers', 'Comment', 'Report Date']
				columns = ['no_of_estinquishers','fire_alarm','status_of_estinguishers','comment','created_at']

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
