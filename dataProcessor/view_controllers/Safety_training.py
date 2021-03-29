from django.shortcuts import render
from rest_framework import viewsets
from dataProcessor.serializers import Safety_trainingSerializer
from dataProcessor.serializers import Safety_trainingSerializer_serializer
from analytics.models import Safety_training
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status


class Safety_trainingViewSet(viewsets.ViewSet):
    def create(self, request):
        queryset = Safety_training.objects.all()

        serializer = Safety_trainingSerializer_serializer(data=request.data)
        # serializer = Storage_facilitySerializer_serializer(request.data, many=True).data

        if serializer.is_valid(raise_exception=True):
            serializer.data['report_name'] = "Zip_1"
            user = User.objects.get(username=serializer.data['username'])
            created_by_id = user.id
            # created_by_id = 4

            queryset = Safety_training.objects.filter(report_name=serializer.data['report_name'])

            status_code = 500
            outData = queryset

            if queryset.exists():
                statusMessage = "Report name already exists"
                return Response({'message': statusMessage}, status=status.HTTP_208_ALREADY_REPORTED)
            else:
                gah_sav = Safety_training(
                    report_name=serializer.data['report_name'],
                    training=serializer.data['training'],
                    no_of_staff=serializer.data['no_of_staff'],
                    no_of_inductions=serializer.data['no_of_inductions'],
                    no_of_visitors=serializer.data['no_of_visitors'],
                    duration=serializer.data['duration'],
                    comment=serializer.data['comment'],
                    created_by_id=created_by_id)

                gah_sav.save()
                status_code= 200
                outData = gah_sav

            return Response(Safety_trainingSerializer(outData).data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)