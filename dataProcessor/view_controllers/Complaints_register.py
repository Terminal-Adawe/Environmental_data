from django.shortcuts import render
from rest_framework import viewsets
from dataProcessor.serializers import Complaints_registerSerializer
from dataProcessor.serializers import Complaints_registerSerializer_serializer
from analytics.models import Complaints_register
from rest_framework.response import Response
from django.contrib.auth.models import User


class Complaints_registerViewSet(viewsets.ViewSet):
    def create(self, request):
        queryset = Complaints_register.objects.all()

        serializer = Complaints_registerSerializer_serializer(data=request.data)
        # serializer = Storage_facilitySerializer_serializer(request.data, many=True).data

        if serializer.is_valid(raise_exception=True):
            serializer.data['report_name'] = "Zip_1"
            user = User.objects.get(username=serializer.data['username'])
            created_by_id = user.id
            # created_by_id = 4

            queryset = Complaints_register.objects.filter(report_name=serializer.data['report_name'])

            status_code = 500
            outData = queryset

            if queryset.exists():
                return Response(Complaints_registerSerializer(outData).data, status=status_code)
            else:
                gah_sav = Complaints_register(
                    report_name=serializer.data['report_name'],
                    no_of_complaints=serializer.data['no_of_complaints'],
                    status_of_complaints=serializer.data['status_of_complaints'],
                    comment=serializer.data['comment'],
                    created_by_id=created_by_id)

                gah_sav.save()
                status_code= 200
                outData = gah_sav

            return Response(Complaints_registerSerializer(outData).data, status=status_code)
        else:
            return Response(status=201)