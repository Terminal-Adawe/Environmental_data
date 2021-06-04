from django.shortcuts import render
from rest_framework import viewsets
from dataProcessor.serializers import Water_managementSerializer
from dataProcessor.serializers import Water_managementSerializer_serializer
from analytics.models import Water_management
from analytics.models import Notifications
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status

from dataProcessor.view_controllers.formulateID import formulate_insert_id
from analytics.view_controllers.notifications import insert_notification


class Water_managementViewSet(viewsets.ViewSet):
    def create(self, request):
        # queryset = Energy_management.objects.all()

        serializer = Water_managementSerializer_serializer(data=request.data)
        # serializer = Storage_facilitySerializer_serializer(request.data, many=True).data

        if serializer.is_valid(raise_exception=True):
            serializer.data['report_name'] = "Zip_1"
            user = User.objects.get(username=serializer.data['username'])
            # created_by_id = user.id
            # created_by_id = 4

            data_save = Water_management(
                    total_water_quantity_available=serializer.data['total_water_quantity_available'],
                    camp_consumption=serializer.data['camp_consumption'],
                    admin_consumption=serializer.data['admin_consumption'],
                    cafeteria_consumption=serializer.data['cafeteria_consumption'],
                    workshop_consumption=serializer.data['workshop_consumption'],
                    mine_plant_consumption=serializer.data['mine_plant_consumption'],
                    other_consumption=serializer.data['other_consumption'],
                    comment=serializer.data['comment'],
                    location=serializer.data['location'],
                    created_by=user)

            data_save.save()
            data_save.report_name = formulate_insert_id(15,str(data_save.id))
            data_save.save()

            insert_notification(19,"Water Management",data_save.report_name,user)

            return Response(Water_managementSerializer(data_save).data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)