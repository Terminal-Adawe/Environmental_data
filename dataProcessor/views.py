from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Storage_facilitySerializer
from .serializers import Storage_facilitySerializer_serializer
from analytics.models import Storage_facility
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from analytics.models import modules
import io
import logging



logger = logging.getLogger("django")

# Create your views here.
# class Storage_facilityViewSet(APIView):
#     def post(self, request, format=None):
#     	data = request.data
#     	print(data)
#     	data.storage_type = "Dam"
#     	queryset = Storage_facility.objects.all()
#     	Storage_facilitySerializer_class = Storage_facilitySerializer(data)

#     	if Storage_facilitySerializer_class.is_valid():
#     		queryset = Storage_facility.objects.all()

class Storage_facilityViewSet(viewsets.ViewSet):
    def create(self, request):
    	queryset = Storage_facility.objects.all()

    	serializer = Storage_facilitySerializer_serializer(data=request.data)
    	# serializer = Storage_facilitySerializer_serializer(request.data, many=True).data

    	if serializer.is_valid(raise_exception=True):
    		storage_type = "Dam"
    		serializer.data['report_name'] = "Zip_1"
    		user = User.objects.get(username=serializer.data['username'])
    		created_by_id = user.id
    		# created_by_id = 4

    		queryset = Storage_facility.objects.filter(storage_type=storage_type,report_name=serializer.data['report_name'])

    		status_code = 500
    		outData = queryset

    		if queryset.exists():
    			pass
    		else:
    			storage_fac = Storage_facility(storage_type=storage_type,
    				report_name=serializer.data['report_name'],
    				status_of_seepage_point=serializer.data['status_of_seepage_point'],
    				stability_of_dam_walls=serializer.data['stability_of_dam_walls'],
    				holding_capacity=serializer.data['holding_capacity'],
    				current_capacity=serializer.data['current_capacity'],
    				spillways_capacity=serializer.data['spillways_capacity'],
    				spillways_stability=serializer.data['spillways_stability'],
    				signs_of_erosion_spillway_tip=serializer.data['signs_of_erosion_spillway_tip'],
    				created_by_id=created_by_id)

    			storage_fac.save()
    			status_code= 200
    			outData = storage_fac

    		return Response(Storage_facilitySerializer(outData).data, status=status_code)
    	else:
    		return Response(status=201)

def get_template(request, module):
    module = module
    queryset = modules.objects.filter(active=1,is_fillable=1)

    url = ''

    if module == "storage_facility":
        url = 'dataProcessor/storage/storage.html'
    elif module == "Grease_and_hydocarbon":
        url = 'dataProcessor/grease_and_hydrocarbon/grease_and_hydrocarbon.html'
    elif module == "Waste_Management":
        url = 'dataProcessor/waste_management/waste_management.html'
    elif module == "Inceneration":
        url = 'dataProcessor/inceneration/inceneration.html'
    elif module == "liquid_waste_and_oil":
        url = 'dataProcessor/liquid_waste_and_oil/liquid_waste_and_oil.html'
    elif module == "health_and_hygiene_awareness":
        url = 'dataProcessor/health_and_hygiene_awareness/health_and_hygiene_awareness.html'
    elif module == "energy_management":
        url = 'dataProcessor/energy_management/energy_management.html'
    elif module == "water_management":
        url = 'dataProcessor/forms/water_management.html'
    elif module == "complaints_register":
        url = 'dataProcessor/forms/complaints_register.html'
    elif module == "slope_stabilization":
        url = 'dataProcessor/forms/slope_stabilization.html'
    elif module == "safety_permission_system":
        url = 'dataProcessor/forms/safety_permission_system.html'
    elif module == "safety_training":
        url = 'dataProcessor/forms/safety_training.html'
    elif module == "safety_tools":
        url = 'dataProcessor/forms/safety_tools.html'
    elif module == "geo_reference":
        url = 'dataProcessor/forms/geoReference.html'
    elif module == "fuel_farm":
        url = 'dataProcessor/forms/fuelFarm.html'
    elif module == "work_env_compliance":
        url = 'dataProcessor/forms/workEnvCompliance.html'
    elif module == "warehouse":
        url = 'dataProcessor/forms/warehouse.html'
    elif module == "conveyers":
        url = 'dataProcessor/forms/conveyers.html'
    elif module == "incident_report":
        url = 'dataProcessor/forms/incidentReport.html'


    logger.info("url is ")
    logger.info(url)

    return render(request, url, {'modules' : queryset, 'module' : module})
        
def storage_facilityView(request):
	queryset = modules.objects.filter(active=1)
	return render(request, 'dataProcessor/storage/storage.html', {'modules' : queryset})

def grease_and_hydrocarbonView(request):
	queryset = modules.objects.filter(active=1)
	return render(request, 'dataProcessor/grease_and_hydrocarbon/grease_and_hydrocarbon.html', {'modules' : queryset})

def waste_managementView(request):
	queryset = modules.objects.filter(active=1)
	return render(request, 'dataProcessor/waste_management/waste_management.html', {'modules' : queryset})

def incenerationView(request):
	queryset = modules.objects.filter(active=1)
	return render(request, 'dataProcessor/inceneration/inceneration.html', {'modules' : queryset})

def liquid_waste_oilView(request):
	queryset = modules.objects.filter(active=1)
	return render(request, 'dataProcessor/liquid_waste_and_oil/liquid_waste_and_oil.html', {'modules' : queryset})

def health_and_hygiene_awarenessView(request):
	queryset = modules.objects.filter(active=1)
	return render(request, 'dataProcessor/health_and_hygiene_awareness/health_and_hygiene_awareness.html', {'modules' : queryset})

def energy_managementView(request):
	queryset = modules.objects.filter(active=1)
	return render(request, 'dataProcessor/energy_management/energy_management.html', {'modules' : queryset})

def water_managementView(request):
    queryset = modules.objects.filter(active=1)
    return render(request, 'dataProcessor/forms/water_management.html', {'modules' : queryset})


def complaints_registerView(request):
	queryset = modules.objects.filter(active=1)
	return render(request, 'dataProcessor/forms/complaints_register.html', {'modules' : queryset})

def slope_stabilizationView(request):
	queryset = modules.objects.filter(active=1)
	return render(request, 'dataProcessor/forms/slope_stabilization.html', {'modules' : queryset})

def safety_permission_systemView(request):
	queryset = modules.objects.filter(active=1)
	return render(request, 'dataProcessor/forms/safety_permission_system.html', {'modules' : queryset})

def safety_trainingView(request):
	queryset = modules.objects.filter(active=1)
	return render(request, 'dataProcessor/forms/safety_training.html', {'modules' : queryset})

def safety_toolsView(request):
	queryset = modules.objects.filter(active=1)
	return render(request, 'dataProcessor/forms/safety_tools.html', {'modules' : queryset})

def geoReferenceView(request):
    queryset = modules.objects.filter(active=1)
    return render(request, 'dataProcessor/forms/geoReference.html', {'modules' : queryset})

def fuelFarmView(request):
    queryset = modules.objects.filter(active=1)
    return render(request, 'dataProcessor/forms/fuelFarm.html', {'modules' : queryset})

def workEnvComplianceView(request):
    queryset = modules.objects.filter(active=1)
    return render(request, 'dataProcessor/forms/workEnvCompliance.html', {'modules' : queryset})

def warehouseView(request):
    queryset = modules.objects.filter(active=1)
    return render(request, 'dataProcessor/forms/warehouse.html', {'modules' : queryset})

def conveyersView(request):
    queryset = modules.objects.filter(active=1)
    return render(request, 'dataProcessor/forms/conveyers.html', {'modules' : queryset})

def incidentReportView(request):
    queryset = modules.objects.filter(active=1)
    return render(request, 'dataProcessor/forms/incidentReport.html', {'modules' : queryset})






