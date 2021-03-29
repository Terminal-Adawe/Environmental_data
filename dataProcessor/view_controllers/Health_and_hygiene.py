from django.shortcuts import render
from rest_framework import viewsets
from dataProcessor.serializers import Health_and_hygiene_awarenessSerializer
from dataProcessor.serializers import Health_and_hygiene_awarenessSerializer_serializer
from analytics.models import Health_and_hygiene_awareness
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status


class Health_and_hygieneViewSet(viewsets.ViewSet):
    def create(self, request):
        queryset = Health_and_hygiene_awarenessSerializer_serializer.objects.all()

        serializer = Liquid_waste_oilSerializer_serializer(data=request.data)
        # serializer = Storage_facilitySerializer_serializer(request.data, many=True).data

        if serializer.is_valid(raise_exception=True):
            serializer.data['report_name'] = "Zip_1"
            user = User.objects.get(username=serializer.data['username'])
            created_by_id = user.id
            # created_by_id = 4

            queryset = Health_and_hygiene_awareness.objects.filter(report_name=serializer.data['report_name'])

            status_code = 500
            outData = queryset

            if queryset.exists():
                statusMessage = "Report name already exists"
                return Response({'message': statusMessage}, status=status.HTTP_208_ALREADY_REPORTED)
            else:
                gah_sav = Health_and_hygiene_awareness(
                    report_name=serializer.data['report_name'],
                    training=serializer.data['training'],
                    no_of_staff=serializer.data['no_of_staff'],
                    duration=serializer.data['duration'],
                    comment=serializer.data['comment'],
                    created_by_id=created_by_id)

                gah_sav.save()
                status_code= 200
                outData = gah_sav

            return Response(Health_and_hygiene_awarenessSerializer(outData).data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)