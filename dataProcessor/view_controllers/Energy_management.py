from django.shortcuts import render
from rest_framework import viewsets
from dataProcessor.serializers import Energy_managementSerializer
from dataProcessor.serializers import Energy_managementSerializer_serializer
from analytics.models import Energy_management
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status


class Energy_managementViewSet(viewsets.ViewSet):
    def create(self, request):
        queryset = Energy_management.objects.all()

        serializer = Energy_managementSerializer_serializer(data=request.data)
        # serializer = Storage_facilitySerializer_serializer(request.data, many=True).data

        if serializer.is_valid(raise_exception=True):
            serializer.data['report_name'] = "Zip_1"
            user = User.objects.get(username=serializer.data['username'])
            created_by_id = user.id
            # created_by_id = 4

            queryset = Energy_management.objects.filter(report_name=serializer.data['report_name'])

            status_code = 500
            outData = queryset

            if queryset.exists():
                statusMessage = "Report name already exists"
                return Response({'message': statusMessage}, status=status.HTTP_208_ALREADY_REPORTED)
            else:
                gah_sav = Energy_management(
                    report_name=serializer.data['report_name'],
                    total_energy_available=serializer.data['total_energy_available'],
                    camp_consumption=serializer.data['camp_consumption'],
                    admin_consumption=serializer.data['admin_consumption'],
                    workshop_consumption=serializer.data['workshop_consumption'],
                    mine_plant_consumption=serializer.data['mine_plant_consumption'],
                    other_consumption=serializer.data['other_consumption'],
                    comment=serializer.data['comment'],
                    created_by_id=created_by_id)

                gah_sav.save()
                status_code= 200
                outData = gah_sav

            return Response(Energy_managementSerializer(outData).data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)