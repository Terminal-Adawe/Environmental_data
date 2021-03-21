from django.shortcuts import render
from rest_framework import viewsets
from dataProcessor.serializers import Waste_managementSerializer
from dataProcessor.serializers import Waste_managementSerializer_serializer
from analytics.models import Waste_Management
from rest_framework.response import Response
from django.contrib.auth.models import User


class Waste_managementViewSet(viewsets.ViewSet):
    def create(self, request):
        queryset = Waste_Management.objects.all()

        serializer = Waste_ManagementSerializer_serializer(data=request.data)
        # serializer = Storage_facilitySerializer_serializer(request.data, many=True).data

        if serializer.is_valid(raise_exception=True):
            serializer.data['report_name'] = "Zip_1"
            user = User.objects.get(username=serializer.data['username'])
            created_by_id = user.id
            # created_by_id = 4

            queryset = Waste_Management.objects.filter(report_name=serializer.data['report_name'])

            status_code = 500
            outData = queryset

            if queryset.exists():
                return Response(Waste_managementSerializer(outData).data, status=status_code)
            else:
                gah_sav = Waste_Management(
                    report_name=serializer.data['report_name'],
                    segregation_at_source_and_bins=serializer.data['segregation_at_source_and_bins'],
                    glass_waste_source=serializer.data['glass_waste_source'],
                    glass_waste_weight=serializer.data['glass_waste_weight'],
                    plastic_waste_source=serializer.data['plastic_waste_source'],
                    plastic_waste_weight=serializer.data['plastic_waste_weight'],
                    metal_waste_source=serializer.data['metal_waste_source'],
                    metal_waste_weight=serializer.data['metal_waste_weight'],
                    comment=serializer.data['comment'],
                    created_by_id=created_by_id)

                gah_sav.save()
                status_code= 200
                outData = gah_sav

            return Response(Waste_managementSerializer(outData).data, status=status_code)
        else:
            return Response(status=201)