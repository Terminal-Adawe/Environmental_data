from django.shortcuts import render
from rest_framework import viewsets
from dataProcessor.serializers import Grease_and_hydrogenSerializer
from dataProcessor.serializers import Grease_and_hydrogenSerializer_serializer
from analytics.models import Grease_and_hydocarbon_spillage
from rest_framework.response import Response
from django.contrib.auth.models import User


class Grease_and_hydrogenViewSet(viewsets.ViewSet):
    def create(self, request):
        queryset = Grease_and_hydocarbon_spillage.objects.all()

        serializer = Grease_and_hydrogenSerializer_serializer(data=request.data)
        # serializer = Storage_facilitySerializer_serializer(request.data, many=True).data

        if serializer.is_valid(raise_exception=True):
            serializer.data['report_name'] = "Zip_1"
            user = User.objects.get(username=serializer.data['username'])
            created_by_id = user.id
            # created_by_id = 4

            queryset = Grease_and_hydocarbon_spillage.objects.filter(report_name=serializer.data['report_name'])

            status_code = 500
            outData = queryset

            if queryset.exists():
                return Response(Grease_and_hydrogenSerializer(outData).data, status=status_code)
            else:
                gah_sav = Grease_and_hydocarbon_spillage(report_name=serializer.data['report_name'],
                  storage_condition=serializer.data['storage_condition'],
                  comment=serializer.data['comment'],
                  created_by_id=created_by_id)

                gah_sav.save()
                status_code= 200
                outData = gah_sav

            return Response(Grease_and_hydrogenSerializer(outData).data, status=status_code)
        else:
            return Response(status=201)
        
        
   
    	
