from django.shortcuts import render
from rest_framework import viewsets
from dataProcessor.serializers import Slope_stabilization_and_surface_water_retentionSerializer
from dataProcessor.serializers import Slope_stabilization_and_surface_water_retentionSerializer_serializer
from analytics.models import Slope_stabilization_and_surface_water_retention
from rest_framework.response import Response
from django.contrib.auth.models import User


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

            queryset = Slope_stabilization_and_surface_water_retention.objects.filter(report_name=serializer.data['report_name'])

            status_code = 500
            outData = queryset

            if queryset.exists():
                return Response(Slope_stabilization_and_surface_water_retentionSerializer(outData).data, status=status_code)
            else:
                gah_sav = Slope_stabilization_and_surface_water_retention(
                    report_name=serializer.data['report_name'],
                    no_of_exposed_unstabilized_slopes=serializer.data['no_of_exposed_unstabilized_slopes'],
                    status=serializer.data['status'],
                    created_by_id=created_by_id)

                gah_sav.save()
                status_code= 200
                outData = gah_sav

            return Response(Slope_stabilization_and_surface_water_retentionSerializer(outData).data, status=status_code)
        else:
            return Response(status=201)