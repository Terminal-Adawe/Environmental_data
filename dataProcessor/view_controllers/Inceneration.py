from django.shortcuts import render
from rest_framework import viewsets
from dataProcessor.serializers import IncenerationSerializer
from dataProcessor.serializers import IncenerationSerializer_serializer
from analytics.models import Waste_Management
from rest_framework.response import Response
from django.contrib.auth.models import User


class IncenerationViewSet(viewsets.ViewSet):
    def create(self, request):
        queryset = Inceneration.objects.all()

        serializer = IncenerationSerializer_serializer(data=request.data)
        # serializer = Storage_facilitySerializer_serializer(request.data, many=True).data

        if serializer.is_valid(raise_exception=True):
            serializer.data['report_name'] = "Zip_1"
            user = User.objects.get(username=serializer.data['username'])
            created_by_id = user.id
            # created_by_id = 4

            queryset = Inceneration.objects.filter(report_name=serializer.data['report_name'])

            status_code = 500
            outData = queryset

            if queryset.exists():
                return Response(IncenerationSerializer(outData).data, status=status_code)
            else:
                gah_sav = Inceneration(
                    report_name=serializer.data['report_name'],
                    items_incenerated=serializer.data['items_incenerated'],
                    quantity=serializer.data['quantity'],
                    temperature=serializer.data['temperature'],
                    comment=serializer.data['comment'],
                    created_by_id=created_by_id)

                gah_sav.save()
                status_code= 200
                outData = gah_sav

            return Response(IncenerationSerializer(outData).data, status=status_code)
        else:
            return Response(status=201)