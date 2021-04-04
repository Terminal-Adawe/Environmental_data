from django.shortcuts import render
from rest_framework import viewsets
from dataProcessor.serializers import Safety_permission_systemSerializer
from dataProcessor.serializers import Safety_permission_systemSerializer_serializer
from analytics.models import Safety_permission_system
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status


class Safety_permission_systemViewSet(viewsets.ViewSet):
    def create(self, request):
        queryset = Safety_permission_system.objects.all()

        serializer = Safety_permission_systemSerializer_serializer(data=request.data)
        # serializer = Storage_facilitySerializer_serializer(request.data, many=True).data

        if serializer.is_valid(raise_exception=True):
            serializer.data['report_name'] = "Zip_1"
            user = User.objects.get(username=serializer.data['username'])
            created_by_id = user.id
            # created_by_id = 4

            queryset = Safety_permission_system.objects.filter(report_name=serializer.data['report_name'])

            status_code = 500
            outData = queryset

            if queryset.exists():
                statusMessage = "Report name already exists"
                return Response({'message': statusMessage}, status=status.HTTP_208_ALREADY_REPORTED)
            else:
                gah_sav = Safety_permission_system(
                    report_name=serializer.data['report_name'],
                    no_of_permits_issued=serializer.data['no_of_permits_issued'],
                    status=serializer.data['status'],
                    comment=serializer.data['comment'],
                    location=serializer.data['location'],
                    created_by_id=created_by_id)

                gah_sav.save()
                status_code= 200
                outData = gah_sav

            return Response(Safety_permission_systemSerializer(outData).data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)