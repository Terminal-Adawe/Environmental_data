from django.shortcuts import render
from rest_framework import viewsets
from analytics.serializers import reportBuilderSerializerGet
from analytics.serializers import randColumnSerializer
from analytics.models import Notifications
from analytics.models import Storage_facility
from analytics.models import Grease_and_hydocarbon_spillage
from analytics.models import Waste_Management
from analytics.models import Inceneration
from analytics.models import Liquid_waste_oil
from analytics.models import Health_and_hygiene_awareness
from analytics.models import Energy_management
from analytics.models import Complaints_register
from analytics.models import Slope_stabilization_and_surface_water_retention
from analytics.models import Safety_training
from analytics.models import Safety_permission_system
from analytics.models import Safety_tools
from analytics.models import GeoReferencePoints
from analytics.models import FuelFarm
from analytics.models import WorkEnvCompliance
from analytics.models import Warehouse
from analytics.models import Conveyers
from analytics.models import IncidentReport
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from django.db.models import Sum
from django.db.models import Count
from django.db.models import F
import logging

from django.http import JsonResponse

from analytics.view_controllers.sys_functions import get_model_using_modulesid

from dataProcessor.view_controllers.formulateID import formulate_insert_id
from analytics.view_controllers.notifications import insert_notification

# Get an instance of a logger
logger = logging.getLogger("module")


class formulateReportViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = reportBuilderSerializerGet(data=request.data)
        # serializer = Storage_facilitySerializer_serializer(request.data, many=True).data

        if serializer.is_valid(raise_exception=True):
            # user = User.objects.get(username=serializer.data['username'])
            # created_by_id = user.id
            # created_by_id = 4

            groupType = serializer.data['groupType']
            module_ = serializer.data['module']
            x_column = serializer.data['x_column']
            y_column = serializer.data['y_column']
            value = serializer.data['value']
            values = x_column

            myModel = get_model_using_modulesid(int(module_))

           
            
            data_ = []

            if y_column is None and x_column is None and value is None:
                return Response("Continue",status=status.HTTP_200_OK)
            elif groupType=="sum":
                if y_column is None and x_column is not None:
                    values=x_column
                    data_ = myModel.objects.values(values).annotate(sum=Sum(value), row=F(values)).values('sum','row')
                elif x_column is None and y_column is not None:
                    values=y_column
                    data_ = myModel.objects.values(values).annotate(sum=Sum(value), column=F(values)).values('sum','column')
                elif x_column is not None and y_column is not None:
                    data_ = myModel.objects.values(y_column,x_column).annotate(sum=Sum(value), row=F(x_column), column=F(y_column)).values('sum','row','column')

            if groupType=="count":
                if y_column is None and x_column is not None:
                    values=x_column
                    data_ = myModel.objects.values(values).annotate(count=Count(value), row=F(values)).values('count','row')
                elif x_column is None and y_column is not None:
                    values=y_column
                    data_ = myModel.objects.values(values).annotate(count=Count(value), column=F(values)).values('count','column')
                elif x_column is not None and y_column is not None:
                    data_ = myModel.objects.values(y_column,x_column).annotate(count=Count(value), row=F(x_column), column=F(y_column)).values('count','row','column')
            #     return Response(JsonResponse(data_,safe=False).data, status=status.HTTP_201_CREATED)
            return Response(data_,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)