from django.shortcuts import render
from rest_framework import viewsets
from dataProcessor.serializers import Storage_facilitySerializer
from dataProcessor.serializers import Storage_facilitySerializer_serializer
from analytics.models import Storage_facility
from analytics.models import Notifications
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status

from dataProcessor.view_controllers.formulateID import formulate_insert_id
from analytics.view_controllers.notifications import insert_notification

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
            user = User.objects.get(username=serializer.data['auth_user'])
            if user.check_password(serializer.data['auth_password']):
                storage_type = "Dam"
    
                user = User.objects.get(username=serializer.data['username'])
                created_by_id = user.id
    		  #created_by_id = 4
            
                data_save = Storage_facility(storage_type=storage_type,
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
    
                data_save.save()
                data_save.report_name = formulate_insert_id(1,str(data_save.id))
                data_save.save()
    
                insert_notification(1,"Storage Facility",data_save.report_name,user)
    
                return Response(Storage_facilitySerializer(data_save).data, status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


