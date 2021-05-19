from django.shortcuts import render
from rest_framework import viewsets
from dataProcessor.serializers import Safety_trainingSerializer
from dataProcessor.serializers import Safety_trainingSerializer_serializer
from analytics.models import Safety_training
from analytics.models import Notifications
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status

from dataProcessor.view_controllers.formulateID import formulate_insert_id
from analytics.view_controllers.notifications import insert_notification


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
            
            data_save = Safety_training(
                    training=serializer.data['training'],
                    no_of_staff=serializer.data['no_of_staff'],
                    no_of_inductions=serializer.data['no_of_inductions'],
                    no_of_visitors=serializer.data['no_of_visitors'],
                    location=serializer.data['location'],
                    duration=serializer.data['duration'],
                    comment=serializer.data['comment'],
                    created_by_id=created_by_id)

            data_save.save()
            data_save.report_name = formulate_insert_id(11,str(data_save.id))
            data_save.save()

            insert_notification(11,"Slope Stabilization and Surface Water Retention",data_save.report_name,user)

            return Response(Safety_trainingSerializer(data_save).data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)