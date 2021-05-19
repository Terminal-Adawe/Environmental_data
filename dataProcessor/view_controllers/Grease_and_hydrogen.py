from django.shortcuts import render
from rest_framework import viewsets
from dataProcessor.serializers import Grease_and_hydrogenSerializer
from dataProcessor.serializers import Grease_and_hydrogenSerializer_serializer
from dataProcessor.serializers import ImageSerializer_serializer
from analytics.models import Grease_and_hydocarbon_spillage
from analytics.models import Notifications
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from analytics.models import Image

from dataProcessor.view_controllers.formulateID import formulate_insert_id
from analytics.view_controllers.notifications import insert_notification


class Grease_and_hydrogenViewSet(viewsets.ViewSet):
    def create(self, request):
        parser_classes = (FormParser, MultiPartParser)
        queryset = Grease_and_hydocarbon_spillage.objects.all()

        serializer = Grease_and_hydrogenSerializer_serializer(data=request.data)
        # image_serializer = ImageSerializer_serializer(data=request.data)
        
        # serializer = Storage_facilitySerializer_serializer(request.data, many=True).data

        if serializer.is_valid(raise_exception=True):
            serializer.data['report_name'] = "Zip_1"
            user = User.objects.get(username=serializer.data['username'])
            created_by_id = user.id

            # queryset = Grease_and_hydocarbon_spillage.objects.filter(report_name=serializer.data['report_name'])

            data_save = Grease_and_hydocarbon_spillage(
                  storage_condition=serializer.data['storage_condition'],
                  comment=serializer.data['comment'],
                  location=serializer.data['location'],
                  created_by_id=created_by_id)

            data_save.save()
            data_save.report_name = formulate_insert_id(15,str(data_save.id))
            data_save.save()
            
            insert_notification(2,"Grease and Hydrocarbon spillage",data_save.report_name,user)

            return Response(Grease_and_hydrogenSerializer(data_save).data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        
   
    	
