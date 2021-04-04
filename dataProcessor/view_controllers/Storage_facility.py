from django.shortcuts import render
from rest_framework import viewsets
from dataProcessor.serializers import Storage_facilitySerializer
from dataProcessor.serializers import Storage_facilitySerializer_serializer
from analytics.models import Storage_facility
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status

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
                statusMessage = "Report name already exists"
                return Response({'message': statusMessage}, status=status.HTTP_208_ALREADY_REPORTED)
            else:
                storage_fac = Storage_facility(storage_type=storage_type,
                    report_name=serializer.data['report_name'],
                    status_of_seepage_point=serializer.data['status_of_seepage_point'],
                    stability_of_dam_walls=serializer.data['stability_of_dam_walls'],
                    holding_capacity=serializer.data['holding_capacity'],
                    comment=serializer.data['comment'],
                    location=serializer.data['location'],
                    current_capacity=serializer.data['current_capacity'],
                    spillways_capacity=serializer.data['spillways_capacity'],
                    spillways_stability=serializer.data['spillways_stability'],
                    signs_of_erosion_spillway_tip=serializer.data['signs_of_erosion_spillway_tip'],
                    created_by_id=created_by_id)

                storage_fac.save()
                status_code= 200
                outData = storage_fac
                return Response(Storage_facilitySerializer(outData).data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


