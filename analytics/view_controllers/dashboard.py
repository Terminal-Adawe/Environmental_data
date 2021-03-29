from django.shortcuts import render
from rest_framework import viewsets
from analytics.serializers import Storage_facilitySerializer
from analytics.serializers import Grease_and_hydrogenSerializer
from analytics.serializers import ComplianceValueSerializer
from dataProcessor.serializers import Waste_ManagementSerializer
from dataProcessor.serializers import IncenerationSerializer
from dataProcessor.serializers import Liquid_waste_oilSerializer
from dataProcessor.serializers import Health_and_hygiene_awarenessSerializer
from dataProcessor.serializers import Energy_managementSerializer
from dataProcessor.serializers import Complaints_registerSerializer
from dataProcessor.serializers import Slope_stabilization_and_surface_water_retentionSerializer
from dataProcessor.serializers import Safety_trainingSerializer
from dataProcessor.serializers import Safety_permission_systemSerializer
from dataProcessor.serializers import Safety_toolsSerializer
from analytics.serializers import ModulesSerializer
from analytics.models import Storage_facility
from analytics.models import ComplianceValue
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
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from drf_multiple_model.views import ObjectMultipleModelAPIView

# class DashboardViewSet(viewsets.ViewSet):
#     def list(self, request):
#     	queryset_1 = Storage_facility.objects.all()
#     	queryset_2 = ComplianceValue.objects.all()

#     	storage_serializer = Storage_facilitySerializer(queryset_1, many=True)

#     	compliancevalue_serializer = ComplianceValue(queryset_2, many=True)

#     	status_code = 200

#     	return Response(storage_serializer.data, status=status_code)

class DashboardViewSet(ObjectMultipleModelAPIView):
		querylist=[
			{'queryset': Storage_facility.objects.all(), 'serializer_class': Storage_facilitySerializer},
			{'queryset': ComplianceValue.objects.all(), 'serializer_class': ComplianceValueSerializer},
			{'queryset': Grease_and_hydocarbon_spillage.objects.all(), 'serializer_class': Grease_and_hydrogenSerializer},
			{'queryset': Waste_Management.objects.all(), 'serializer_class': Waste_ManagementSerializer},
			{'queryset': Inceneration.objects.all(), 'serializer_class': IncenerationSerializer},
			{'queryset': Liquid_waste_oil.objects.all(), 'serializer_class': Liquid_waste_oilSerializer},
			{'queryset': Health_and_hygiene_awareness.objects.all(), 'serializer_class': Health_and_hygiene_awarenessSerializer},
			{'queryset': Energy_management.objects.all(), 'serializer_class': Energy_managementSerializer},
			{'queryset': Complaints_register.objects.all(), 'serializer_class': Complaints_registerSerializer},
			{'queryset': Slope_stabilization_and_surface_water_retention.objects.all(), 'serializer_class': Slope_stabilization_and_surface_water_retentionSerializer},
			{'queryset': Safety_training.objects.all(), 'serializer_class': Safety_trainingSerializer},
			{'queryset': Safety_permission_system.objects.all(), 'serializer_class': Safety_permission_systemSerializer},
			{'queryset': Safety_tools.objects.all(), 'serializer_class': Safety_toolsSerializer},
			{'queryset': modules.objects.all(), 'serializer_class': ModulesSerializer},
		]
