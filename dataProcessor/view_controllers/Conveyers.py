from django.shortcuts import render
from rest_framework import viewsets
from dataProcessor.serializers import ConveyersSerializer
from dataProcessor.serializers import ConveyersSerializer_serializer
from analytics.models import Conveyers
from analytics.models import Notifications
from analytics.models import NotificationViewer
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status

from dataProcessor.view_controllers.formulateID import formulate_insert_id
from analytics.view_controllers.notifications import insert_notification


class ConveyersViewSet(viewsets.ViewSet):
    def create(self, request):
        queryset = WorkEnvCompliance.objects.all()

        serializer = WorkEnvComplianceSerializer_serializer(data=request.data)
        # serializer = Storage_facilitySerializer_serializer(request.data, many=True).data

        if serializer.is_valid(raise_exception=True):
            user = User.objects.get(username=serializer.data['auth_user'])
            if user.check_password(serializer.data['auth_password']):
                user = User.objects.get(username=serializer.data['username'])
                created_by_id = user.id
                # created_by_id = 4
    
                # queryset = GeoReferencePoints.objects.filter(report_name=serializer.data['report_name'])
    
                data_save = WorkEnvCompliance(
                        first_aid=serializer.data['first_aid'],
                        safety_stickers=serializer.data['safety_stickers'],
                        fire_alarm=serializer.data['fire_alarm'],
                        flooding=serializer.data['flooding'],
                        flammables=serializer.data['flammables'],
                        no_of_estinquishers=serializer.data['no_of_estinquishers'],
                        comment=serializer.data['comment'],
                        location=serializer.data['location'],
                        created_by_id=created_by_id)
    
                data_save.save()
                data_save.report_name = formulate_insert_id(17,str(data_save.id))
                data_save.save()
    
                insert_notification(17,"Conveyers",data_save.report_name,user)
    
                return Response(WorkEnvComplianceSerializer(data_save).data, status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)