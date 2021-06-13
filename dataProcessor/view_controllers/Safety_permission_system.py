from django.shortcuts import render
from rest_framework import viewsets
from dataProcessor.serializers import Safety_permission_systemSerializer
from dataProcessor.serializers import Safety_permission_systemSerializer_serializer
from analytics.models import Safety_permission_system
from analytics.models import Notifications
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status

from dataProcessor.view_controllers.formulateID import formulate_insert_id
from analytics.view_controllers.notifications import insert_notification


class Safety_permission_systemViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = Safety_permission_systemSerializer_serializer(data=request.data)
        # serializer = Storage_facilitySerializer_serializer(request.data, many=True).data

        if serializer.is_valid(raise_exception=True):
            user = User.objects.get(username=serializer.data['auth_user'])
            if user.check_password(serializer.data['auth_password']):
                serializer.data['report_name'] = "Zip_1"
                user = User.objects.get(username=serializer.data['username'])
                created_by_id = user.id
                # created_by_id = 4
    
    
                data_save = Safety_permission_system(
                        no_of_permits_issued=serializer.data['no_of_permits_issued'],
                        status=serializer.data['status'],
                        comment=serializer.data['comment'],
                        location=serializer.data['location'],
                        created_by_id=created_by_id)
    
                data_save.save()
                data_save.report_name = formulate_insert_id(15,str(data_save.id))
                data_save.save()
    
                insert_notification(10,"Safety Permission System",data_save.report_name,user)
    
                return Response(Safety_permission_systemSerializer(data_save).data, status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)