from django.shortcuts import render
from rest_framework import viewsets
from dataProcessor.serializers import Liquid_waste_oilSerializer
from dataProcessor.serializers import Liquid_waste_oilSerializer_serializer
from analytics.models import Liquid_waste_oil
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status


class liquid_waste_oilViewSet(viewsets.ViewSet):
    def create(self, request):
        queryset = Liquid_waste_oil.objects.all()

        serializer = Liquid_waste_oilSerializer_serializer(data=request.data)
        # serializer = Storage_facilitySerializer_serializer(request.data, many=True).data

        if serializer.is_valid(raise_exception=True):
            serializer.data['report_name'] = "Zip_1"
            user = User.objects.get(username=serializer.data['username'])
            created_by_id = user.id
            # created_by_id = 4

            queryset = Liquid_waste_oil.objects.filter(report_name=serializer.data['report_name'])

            status_code = 500
            outData = queryset

            if queryset.exists():
                statusMessage = "Report name already exists"
                return Response({'message': statusMessage}, status=status.HTTP_208_ALREADY_REPORTED)
            else:
                gah_sav = Liquid_waste_oil(
                    report_name=serializer.data['report_name'],
                    discharge_point=serializer.data['discharge_point'],
                    source=serializer.data['source'],
                    comment=serializer.data['comment'],
                    created_by_id=created_by_id)

                gah_sav.save()
                status_code= 200
                outData = gah_sav

            return Response(Liquid_waste_oilSerializer(outData).data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)