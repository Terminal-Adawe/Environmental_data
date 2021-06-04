from django.shortcuts import render
from rest_framework import viewsets
from dataProcessor.serializers import Waste_ManagementSerializer
from dataProcessor.serializers import Waste_ManagementSerializer_serializer
from analytics.models import Waste_Management
from analytics.models import WasteDetails
from analytics.models import NotificationViewer
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
import logging

from dataProcessor.view_controllers.formulateID import formulate_insert_id
from analytics.view_controllers.notifications import insert_notification


# Get an instance of a logger
logger = logging.getLogger("django")


class Waste_managementViewSet(viewsets.ViewSet):
    def create(self, request):
        queryset = Waste_Management.objects.all()

        serializer = Waste_ManagementSerializer_serializer(data=request.data)
        # serializer = Storage_facilitySerializer_serializer(request.data, many=True).data

        if serializer.is_valid(raise_exception=True):
            user = User.objects.get(username=serializer.data['auth_user'])
            if user.check_password(serializer.data['auth_password']):
                user = User.objects.get(username=serializer.data['username'])
                created_by_id = user.id
                # created_by_id = 4
    
                glassSource = serializer.data['glass_waste_source']
                glassWeight = serializer.data['glass_waste_weight']
                logger.debug(glassWeight)
                i=0
                for item in glassSource:
                    weight = glassWeight[i][1]
                    logger.debug("Weight is ")
                    logger.debug(weight)
                    if glassWeight[i][1]=='':
                        weight = 0
                    else:
                        weight = int(glassWeight[i][1])
                    save_item = WasteDetails(
                        waste_type="Glass",
                        waste_source=item[1],
                        waste_weightage=weight,
                        created_by_id=created_by_id
                        )
                    i += 1
                    save_item.save()
                
                logger.error("Error processings")
                logger.debug(glassWeight)
                data_save = Waste_Management(
                    report_name=serializer.data['report_name'],
                    segregation_at_source_and_bins=serializer.data['segregation_at_source_and_bins'],
                    location=serializer.data['location'],
                    comment=serializer.data['comment'],
                    created_by_id=created_by_id)
                data_save.save()
                data_save.report_name = formulate_insert_id(15,str(data_save.id))
                data_save.save()
                insert_notification(3,"Waste Management",data_save.report_name,user)
                return Response(Waste_ManagementSerializer(data_save).data, status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.validated_data, status=status.HTTP_400_BAD_REQUEST)