from django.shortcuts import render
from rest_framework import viewsets
from dataProcessor.serializers import Complaints_registerSerializer
from dataProcessor.serializers import Complaints_registerSerializer_serializer
from analytics.models import Complaints_register
from analytics.models import Notifications
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status

from dataProcessor.view_controllers.formulateID import formulate_insert_id
from analytics.view_controllers.notifications import insert_notification


class Complaints_registerViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = Complaints_registerSerializer_serializer(data=request.data)
        # serializer = Storage_facilitySerializer_serializer(request.data, many=True).data

        if serializer.is_valid(raise_exception=True):
            user = User.objects.get(username=serializer.data['auth_user'])
            if user.check_password(serializer.data['auth_password']):
                serializer.data['report_name'] = "Zip_1"
                user = User.objects.get(username=serializer.data['username'])
                created_by_id = user.id
                # created_by_id = 4

                data_save = Complaints_register(
                        no_of_complaints=serializer.data['no_of_complaints'],
                        status_of_complaints=serializer.data['status_of_complaints'],
                        comment=serializer.data['comment'],
                        location=serializer.data['location'],
                        created_by_id=created_by_id)

                data_save.save()
                data_save.report_name = formulate_insert_id(8,str(data_save.id))
                data_save.save()
                
                insert_notification(8,"Complaints Register",data_save.report_name,user)
    
                return Response(Complaints_registerSerializer(data_save).data, status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)