from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework import viewsets

from analytics.models import ComplianceValue
from analytics.models import modules
from analytics.models import Image
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
from analytics.models import Graph_config

from analytics.serializers import ModulesSerializer
from analytics.serializers import formSerializer
from rest_framework import status

import logging

logger = logging.getLogger("django")


class postRequestViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = formSerializer(data=request.data)

        

        if serializer.is_valid(raise_exception=True):
            logger.info("data is ")
            # data_json = json.loads(serializer.data['fields'][0])
            logger.info(serializer.data['fields'])
            for x in serializer.data['fields']:
                logger.info("other data is ")
                logger.info(x['stability_of_dam_walls'])
            # user = User.objects.get(username=serializer.data['auth_user'])
            # if user.check_password(serializer.data['auth_password']):
            queryset = modules.objects.all()
            return Response("successful",status.HTTP_202_ACCEPTED)
            # else:
            #     return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)