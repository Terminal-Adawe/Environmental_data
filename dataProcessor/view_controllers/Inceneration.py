from django.shortcuts import render
from rest_framework import viewsets
from dataProcessor.serializers import IncenerationSerializer
from dataProcessor.serializers import IncenerationSerializer_serializer
from analytics.models import Inceneration
from analytics.models import Notifications
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status

from dataProcessor.view_controllers.formulateID import formulate_insert_id
from analytics.view_controllers.notifications import insert_notification


class IncenerationViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = IncenerationSerializer_serializer(data=request.data)
        # serializer = Storage_facilitySerializer_serializer(request.data, many=True).data

        if serializer.is_valid(raise_exception=True):
            user = User.objects.get(username=serializer.data['auth_user'])
            if user.check_password(serializer.data['auth_password']):
                serializer.data['report_name'] = "Zip_1"
                user = User.objects.get(username=serializer.data['username'])
                created_by_id = user.id
                # created_by_id = 4
    
                queryset = Inceneration.objects.filter(report_name=serializer.data['report_name'])
            
                data_save = Inceneration(
                        items_incenerated=serializer.data['items_incenerated'],
                        quantity=serializer.data['quantity'],
                        temperature=serializer.data['temperature'],
                        comment=serializer.data['comment'],
                        location=serializer.data['location'],
                        created_by_id=created_by_id)
    
                data_save.save()
                data_save.report_name = formulate_insert_id(4,str(data_save.id))
                data_save.save()
    
                insert_notification(4,"Inceneration",data_save.report_name,user)
    
                return Response(IncenerationSerializer(data_save).data, status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)