from django.shortcuts import render
from rest_framework import viewsets
from analytics.serializers import Storage_facilitySerializer
from analytics.serializers import Grease_and_hydrogenSerializer
from analytics.serializers import ComplianceValueSerializer
from analytics.models import Storage_facility
from analytics.models import ComplianceValue
from analytics.models import Grease_and_hydocarbon_spillage
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from drf_multiple_model.views import ObjectMultipleModelAPIView


from analytics.models import ComplianceValue

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
		]
