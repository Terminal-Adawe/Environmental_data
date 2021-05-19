from django.shortcuts import render
from rest_framework import viewsets
from dataProcessor.serializers import Health_and_hygiene_awarenessSerializer
from dataProcessor.serializers import Health_and_hygiene_awarenessSerializer_serializer
from analytics.models import Health_and_hygiene_awareness
from analytics.models import Notifications
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status

from dataProcessor.view_controllers.formulateID import formulate_insert_id
from analytics.view_controllers.notifications import insert_notification


class Health_and_hygieneViewSet(viewsets.ViewSet):
    def create(self, request):
        queryset = Health_and_hygiene_awareness.objects.all()

        serializer = Health_and_hygiene_awarenessSerializer_serializer(data=request.data)
        # serializer = Storage_facilitySerializer_serializer(request.data, many=True).data

        if serializer.is_valid(raise_exception=True):
            serializer.data['report_name'] = "Zip_1"
            user = User.objects.get(username=serializer.data['username'])
            created_by_id = user.id
            # created_by_id = 4

            data_save = Health_and_hygiene_awareness(
                    training=serializer.data['training'],
                    no_of_staff=serializer.data['no_of_staff'],
                    duration=serializer.data['duration'],
                    comment=serializer.data['comment'],
                    location=serializer.data['location'],
                    created_by_id=created_by_id)

            data_save.save()
            data_save.report_name = formulate_insert_id(15,str(data_save.id))
            data_save.save()
            
            insert_notification(6,"Health and Hygeine",data_save.report_name,user)

            return Response(Health_and_hygiene_awarenessSerializer(data_save).data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)