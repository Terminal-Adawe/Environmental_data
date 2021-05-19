from django.shortcuts import render
from rest_framework import viewsets
from dataProcessor.serializers import Slope_stabilization_and_surface_water_retentionSerializer
from dataProcessor.serializers import Slope_stabilization_and_surface_water_retentionSerializer_serializer
from analytics.models import Slope_stabilization_and_surface_water_retention
from analytics.models import Notifications
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status

from dataProcessor.view_controllers.formulateID import formulate_insert_id
from analytics.view_controllers.notifications import insert_notification


class Slope_stabilization_and_surface_water_retentionViewSet(viewsets.ViewSet):
    def create(self, request):
        queryset = Slope_stabilization_and_surface_water_retention.objects.all()

        serializer = Slope_stabilization_and_surface_water_retentionSerializer_serializer(data=request.data)
        # serializer = Storage_facilitySerializer_serializer(request.data, many=True).data

        if serializer.is_valid(raise_exception=True):
            serializer.data['report_name'] = "Zip_1"
            user = User.objects.get(username=serializer.data['username'])
            created_by_id = user.id
            # created_by_id = 4

            data_save = Slope_stabilization_and_surface_water_retention(
                    no_of_exposed_unstabilized_slopes=serializer.data['no_of_exposed_unstabilized_slopes'],
                    status=serializer.data['status'],
                    location=serializer.data['location'],
                    created_by_id=created_by_id)

            data_save.save()

            data_save.report_name = formulate_insert_id(9,str(data_save.id))
            data_save.save()

            insert_notification(9,"Slope Stabilization and Surface water retention",data_save.report_name,user)

            return Response(Slope_stabilization_and_surface_water_retentionSerializer(data_save).data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)