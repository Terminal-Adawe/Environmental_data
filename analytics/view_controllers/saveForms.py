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
from analytics.models import WasteDetails

from analytics.serializers import ModulesSerializer
from analytics.serializers import formSerializer
from dataProcessor.serializers import Complaints_registerSerializer
from dataProcessor.serializers import Complaints_registerSerializer_serializer
from dataProcessor.serializers import Storage_facilitySerializer
from dataProcessor.serializers import Storage_facilitySerializer_serializer
from dataProcessor.serializers import Grease_and_hydrogenSerializer
from dataProcessor.serializers import Grease_and_hydrogenSerializer_serializer
from dataProcessor.serializers import IncenerationSerializer
from dataProcessor.serializers import IncenerationSerializer_serializer
from dataProcessor.serializers import Waste_ManagementSerializer
from dataProcessor.serializers import Waste_ManagementSerializer_serializer_alt
from dataProcessor.serializers import Water_managementSerializer
from dataProcessor.serializers import Water_managementSerializer_serializer
from dataProcessor.serializers import WorkEnvComplianceSerializer
from dataProcessor.serializers import WorkEnvComplianceSerializer_serializer
from dataProcessor.serializers import WarehouseSerializer
from dataProcessor.serializers import WarehouseSerializer_serializer
from dataProcessor.serializers import Slope_stabilization_and_surface_water_retentionSerializer
from dataProcessor.serializers import Slope_stabilization_and_surface_water_retentionSerializer_serializer
from dataProcessor.serializers import Safety_trainingSerializer
from dataProcessor.serializers import Safety_trainingSerializer_serializer
from dataProcessor.serializers import Safety_toolsSerializer
from dataProcessor.serializers import Safety_toolsSerializer_serializer
from dataProcessor.serializers import Safety_permission_systemSerializer
from dataProcessor.serializers import Safety_permission_systemSerializer_serializer
from dataProcessor.serializers import Liquid_waste_oilSerializer
from dataProcessor.serializers import Liquid_waste_oilSerializer_serializer
from dataProcessor.serializers import IncidentReportSerializer
from dataProcessor.serializers import IncidentReportSerializer_serializer
from dataProcessor.serializers import ImageSerializer_serializer
from dataProcessor.serializers import ImageSerializer
from dataProcessor.serializers import Health_and_hygiene_awarenessSerializer
from dataProcessor.serializers import Health_and_hygiene_awarenessSerializer_serializer
from dataProcessor.serializers import GeoReferencePointsSerializer
from dataProcessor.serializers import GeoReferencePointsSerializer_serializer
from dataProcessor.serializers import Energy_managementSerializer
from dataProcessor.serializers import Energy_managementSerializer_serializer
from dataProcessor.serializers import ConveyersSerializer
from dataProcessor.serializers import ConveyersSerializer_serializer

from rest_framework import status


from dataProcessor.view_controllers.formulateID import formulate_insert_id
from analytics.view_controllers.notifications import insert_notification

import logging

logger = logging.getLogger("django")

def save_waste_details(report_name, waste_type, source, weight, created_by):
    save_item = WasteDetails(
                    report_name=report_name,
                    waste_type=waste_type,
                    waste_source=source,
                    waste_weightage=weight,
                    created_by=created_by
                            )

    save_item.save()

def storage_facility_func(payload, additionalFields):
    logger.info("data is ")
    logger.info(payload)
    serializer = Storage_facilitySerializer_serializer(data=payload)
        # serializer = Storage_facilitySerializer_serializer(request.data, many=True).data

    if serializer.is_valid(raise_exception=True):
        user = User.objects.get(username=serializer.data['auth_user'])
        if user.check_password(serializer.data['auth_password']):
            storage_type = "Dam"
    
            user = User.objects.get(username=serializer.data['username'])
            created_by_id = user.id
              #created_by_id = 4
            
            data_save = Storage_facility(storage_type=storage_type,
                        status_of_seepage_point=serializer.data['status_of_seepage_point'],
                        stability_of_dam_walls=serializer.data['stability_of_dam_walls'],
                        holding_capacity=serializer.data['holding_capacity'],
                        comment=serializer.data['comments'],
                        location=serializer.data['location'],
                        current_capacity=serializer.data['current_capacity'],
                        spillways_capacity=serializer.data['spillways_capacity'],
                        spillways_stability=serializer.data['spillways_stability'],
                        signs_of_erosion_spillway_tip=serializer.data['signs_of_erosion_spillway_tip'],
                        created_by_id=created_by_id)
    
            data_save.save()
            data_save.report_name = formulate_insert_id(1,str(data_save.id))
            data_save.save()
    
            insert_notification(1,"Storage Facility",data_save.report_name,user)
    
            response_back = {
                'status_code': status.HTTP_201_CREATED,
                'status_message': "successfully inserted"
            }

            return response_back
        else:
            return status.HTTP_401_UNAUTHORIZED
    else:
        return status.HTTP_400_BAD_REQUEST

def Grease_and_hydocarbon_func(payload, additionalFields):
    serializer = Grease_and_hydrogenSerializer_serializer(data=payload)
        # image_serializer = ImageSerializer_serializer(data=request.data)
        
        # serializer = Storage_facilitySerializer_serializer(request.data, many=True).data

    if serializer.is_valid(raise_exception=True):
        user = User.objects.get(username=serializer.data['auth_user'])
        if user.check_password(serializer.data['auth_password']):
            serializer.data['report_name'] = "Zip_1"
            user = User.objects.get(username=serializer.data['username'])
            created_by_id = user.id

            # queryset = Grease_and_hydocarbon_spillage.objects.filter(report_name=serializer.data['report_name'])

            data_save = Grease_and_hydocarbon_spillage(
                  storage_condition=serializer.data['storage_condition'],
                  comment=serializer.data['comments'],
                  location=serializer.data['location'],
                  created_by_id=created_by_id)

            data_save.save()
            data_save.report_name = formulate_insert_id(15,str(data_save.id))
            data_save.save()
            
            insert_notification(2,"Grease and Hydrocarbon spillage",data_save.report_name,user)

            response_back = {
                'status_code': status.HTTP_201_CREATED,
                'status_message': "successfully inserted"
            }

            return response_back
        else:
            return status.HTTP_401_UNAUTHORIZED
    else:
        return status.HTTP_400_BAD_REQUEST


def Waste_Management_func(payload, additionalFields):
    logger.info("payload data is ")
    logger.info(payload)
    serializer = Waste_ManagementSerializer_serializer_alt(data=payload)
        # serializer = Storage_facilitySerializer_serializer(request.data, many=True).data

    if serializer.is_valid(raise_exception=True):
        user = User.objects.get(username=serializer.data['auth_user'])
        if user.check_password(serializer.data['auth_password']):
            user = User.objects.get(username=serializer.data['username'])
            created_by_id = user.id
            # created_by_id = 4

            logger.info("Waste Management data is ")
            logger.info(serializer.data)

            data_save = Waste_Management(
                segregation_at_source_and_bins=serializer.data['segregation_at_source_and_bins'],
                location=serializer.data['location'],
                comment=serializer.data['comments'],
                created_by=user)
            data_save.save()
            data_save.report_name = formulate_insert_id(3,str(data_save.id))
            data_save.save()
            insert_notification(3,"Waste Management",data_save.report_name,user)

            glassSource = serializer.data['glass_waste_source']
            glassWeight = serializer.data['glass_waste_weight']

            save_waste_details(data_save.report_name, "Glass", glassSource, glassWeight, user)

            logger.debug(glassWeight)


            #Save Organic Details
            organicSource = serializer.data['organic_waste_source']
            organicWeight = serializer.data['organic_waste_weight']

            save_waste_details(data_save.report_name, "Organic", organicSource, organicWeight, user)


            #Save Plastic Details
            plasticSource = serializer.data['plastic_waste_source']
            plasticWeight = serializer.data['plastic_waste_weight']

            save_waste_details(data_save.report_name, "Plastic", plasticSource, plasticWeight, user)

            #Save Metal Details
            metalSource = serializer.data['metal_waste_source']
            metalWeight = serializer.data['metal_waste_weight']

            save_waste_details(data_save.report_name, "Metal", metalSource, metalWeight, user)

            response_back = {
                'status_code': status.HTTP_201_CREATED,
                'status_message': "successfully inserted"
            }

            if additionalFields:
                # logger.info("Waste Management additional fields are ")
                # logger.info(additionalFields[0])

                additional_field_list = additionalFields[0]

                for obj in additional_field_list:
                    logger.info("Additional field is  ")
                    logger.info(obj)

                    if 'OrganicWasteSource' in obj:
                        source = obj['OrganicWasteSource']
                        weight = obj['OrganicWasteWt']

                        save_waste_details(data_save.report_name, "Organic", source, weight, user)

                    if 'PlasticWasteSource' in obj:
                        source = obj['PlasticWasteSource']
                        weight = obj['PlasticWasteWt']

                        save_waste_details(data_save.report_name, "Plastic", source, weight, user)

                    if 'GlassWasteSource' in obj:
                        source = obj['GlassWasteSource']
                        weight = obj['GlassWasteWt']

                        save_waste_details(data_save.report_name, "Glass", source, weight, user)

                    if 'MetalWasteSource' in obj:
                        source = obj['MetalWasteSource']
                        weight = obj['MetalWasteWt']

                        save_waste_details(data_save.report_name, "Metal", source, weight, user)

            return response_back
        else:
            return status.HTTP_401_UNAUTHORIZED
    else:
        return status.HTTP_400_BAD_REQUEST

def Inceneration_func(payload, additionalFields):
    serializer = IncenerationSerializer_serializer(data=payload)
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
                    comment=serializer.data['comments'],
                    location=serializer.data['location'],
                    created_by_id=created_by_id)

            data_save.save()
            data_save.report_name = formulate_insert_id(15,str(data_save.id))
            data_save.save()

            insert_notification(4,"Inceneration",data_save.report_name,user)

            return Response(IncenerationSerializer(data_save).data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

def liquid_waste_and_oil_func(payload, additionalFields):
    serializer = Liquid_waste_oilSerializer_serializer(data=payload)
    # serializer = Storage_facilitySerializer_serializer(request.data, many=True).data
    if serializer.is_valid(raise_exception=True):
        user = User.objects.get(username=serializer.data['auth_user'])
        if user.check_password(serializer.data['auth_password']):
            serializer.data['report_name'] = "Zip_1"
            user = User.objects.get(username=serializer.data['username'])
            created_by_id = user.id
            # created_by_id = 4

            data_save = Liquid_waste_oil(
                    discharge_point=serializer.data['discharge_point'],
                    source=serializer.data['source'],
                    comment=serializer.data['comments'],
                    location=serializer.data['location'],
                    created_by_id=created_by_id)

            data_save.save()
            data_save.report_name = formulate_insert_id(15,str(data_save.id))
            data_save.save()
            
            insert_notification(5,"Liquid Waste Oil",data_save.report_name,user)

            response_back = {
                'status_code': status.HTTP_201_CREATED,
                'status_message': "successfully inserted"
            }

            return response_back
        else:
            return status.HTTP_401_UNAUTHORIZED
    else:
        return status.HTTP_400_BAD_REQUEST

def health_and_hygiene_awareness_func(payload, additionalFields):
    queryset = Health_and_hygiene_awareness.objects.all()
    serializer = Health_and_hygiene_awarenessSerializer_serializer(data=payload)
    # serializer = Storage_facilitySerializer_serializer(request.data, many=True).data
    if serializer.is_valid(raise_exception=True):
        user = User.objects.get(username=serializer.data['auth_user'])
        if user.check_password(serializer.data['auth_password']):
            serializer.data['report_name'] = "Zip_1"
            user = User.objects.get(username=serializer.data['username'])
            created_by_id = user.id
            # created_by_id = 4

            data_save = Health_and_hygiene_awareness(
                    training=serializer.data['training'],
                    no_of_staff=serializer.data['no_of_staff'],
                    duration=serializer.data['duration'],
                    comment=serializer.data['comments'],
                    location=serializer.data['location'],
                    created_by_id=created_by_id)

            data_save.save()
            data_save.report_name = formulate_insert_id(15,str(data_save.id))
            data_save.save()
            
            insert_notification(6,"Health and Hygeine",data_save.report_name,user)

            response_back = {
                'status_code': status.HTTP_201_CREATED,
                'status_message': "successfully inserted"
            }

            return response_back
        else:
            return status.HTTP_401_UNAUTHORIZED
    else:
        return status.HTTP_400_BAD_REQUEST

def energy_management_func(payload, additionalFields):
    serializer = Energy_managementSerializer_serializer(data=payload)
    # serializer = Storage_facilitySerializer_serializer(request.data, many=True).data
    if serializer.is_valid(raise_exception=True):
        user = User.objects.get(username=serializer.data['auth_user'])
        if user.check_password(serializer.data['auth_password']):
            serializer.data['report_name'] = "Zip_1"
            user = User.objects.get(username=serializer.data['username'])
            created_by_id = user.id
            # created_by_id = 4

            data_save = Energy_management(
                    total_energy_available=serializer.data['total_energy_available'],
                    camp_consumption=serializer.data['camp_consumption'],
                    admin_consumption=serializer.data['admin_consumption'],
                    workshop_consumption=serializer.data['workshop_consumption'],
                    mine_plant_consumption=serializer.data['mine_plant_consumption'],
                    other_consumption=serializer.data['other_consumption'],
                    comment=serializer.data['comments'],
                    location=serializer.data['location'],
                    created_by_id=created_by_id)

            data_save.save()
            data_save.report_name = formulate_insert_id(15,str(data_save.id))
            data_save.save()

            insert_notification(7,"Energy Management",data_save.report_name,user)

            response_back = {
                'status_code': status.HTTP_201_CREATED,
                'status_message': "successfully inserted"
            }

            return response_back
        else:
            return status.HTTP_401_UNAUTHORIZED
    else:
        return status.HTTP_400_BAD_REQUEST

def complaints_register_func(payload, additionalFields):
    serializer = Complaints_registerSerializer_serializer(data=payload)
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
                    comment=serializer.data['comments'],
                    location=serializer.data['location'],
                    created_by_id=created_by_id)
            data_save.save()
            data_save.report_name = formulate_insert_id(15,str(data_save.id))
            data_save.save()
            
            insert_notification(8,"Complaints Register",data_save.report_name,user)

            response_back = {
                'status_code': status.HTTP_201_CREATED,
                'status_message': "successfully inserted"
            }

            return response_back
        else:
            return status.HTTP_401_UNAUTHORIZED
    else:
        return status.HTTP_400_BAD_REQUEST

def slope_stabilization_func(payload, additionalFields):
    serializer = Slope_stabilization_and_surface_water_retentionSerializer_serializer(data=payload)
    # serializer = Storage_facilitySerializer_serializer(request.data, many=True).data
    if serializer.is_valid(raise_exception=True):
        user = User.objects.get(username=serializer.data['auth_user'])
        if user.check_password(serializer.data['auth_password']):
            user = User.objects.get(username=serializer.data['username'])
            created_by_id = user.id
            # created_by_id = 4

            data_save = Slope_stabilization_and_surface_water_retention(
                    no_of_exposed_unstabilized_slopes=serializer.data['no_of_exposed_unstabilized_slopes'],
                    status=serializer.data['status'],
                    location=serializer.data['location'],
                    comment=serializer.data['comments'],
                    created_by_id=created_by_id)

            data_save.save()

            data_save.report_name = formulate_insert_id(9,str(data_save.id))
            data_save.save()

            insert_notification(9,"Slope Stabilization and Surface water retention",data_save.report_name,user)

            response_back = {
                'status_code': status.HTTP_201_CREATED,
                'status_message': "successfully inserted"
            }

            return response_back
        else:
            return status.HTTP_401_UNAUTHORIZED
    else:
        return status.HTTP_400_BAD_REQUEST

def safety_permission_system_func(payload, additionalFields):
    serializer = Safety_permission_systemSerializer_serializer(data=payload)
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
                    comment=serializer.data['comments'],
                    location=serializer.data['location'],
                    created_by_id=created_by_id)

            data_save.save()
            data_save.report_name = formulate_insert_id(15,str(data_save.id))
            data_save.save()

            insert_notification(10,"Safety Permission System",data_save.report_name,user)

            response_back = {
                'status_code': status.HTTP_201_CREATED,
                'status_message': "successfully inserted"
            }

            return response_back
        else:
            return status.HTTP_401_UNAUTHORIZED
    else:
        return status.HTTP_400_BAD_REQUEST

def safety_training_func(payload, additionalFields):
    queryset = Safety_training.objects.all()
    serializer = Safety_trainingSerializer_serializer(data=payload)
    # serializer = Storage_facilitySerializer_serializer(request.data, many=True).data
    if serializer.is_valid(raise_exception=True):
        user = User.objects.get(username=serializer.data['auth_user'])
        if user.check_password(serializer.data['auth_password']):
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
                    comment=serializer.data['comments'],
                    created_by_id=created_by_id)

            data_save.save()
            data_save.report_name = formulate_insert_id(11,str(data_save.id))
            data_save.save()

            insert_notification(11,"Slope Stabilization and Surface Water Retention",data_save.report_name,user)

            response_back = {
                'status_code': status.HTTP_201_CREATED,
                'status_message': "successfully inserted"
            }

            return response_back
        else:
            return status.HTTP_401_UNAUTHORIZED
    else:
        return status.HTTP_400_BAD_REQUEST

def safety_tools_func(payload, additionalFields):
    # queryset = Safety_tools.objects.all()
    serializer = Safety_toolsSerializer_serializer(data=payload)
    # serializer = Storage_facilitySerializer_serializer(request.data, many=True).data
    if serializer.is_valid(raise_exception=True):
        user = User.objects.get(username=serializer.data['auth_user'])
        if user.check_password(serializer.data['auth_password']):
            serializer.data['report_name'] = "Zip_1"
            user = User.objects.get(username=serializer.data['username'])
            created_by_id = user.id
            # created_by_id = 4


            data_save = Safety_tools(
                    no_of_estinquishers=serializer.data['no_of_estinquishers'],
                    fire_alarm=serializer.data['fire_alarm'],
                    status_of_estinguishers=serializer.data['status_of_estinguishers'],
                    comment=serializer.data['comments'],
                    location=serializer.data['location'],
                    created_by_id=created_by_id)

            data_save.save()
            data_save.report_name = formulate_insert_id(15,str(data_save.id))
            data_save.save()

            insert_notification(12,"Safety Tools",data_save.report_name,user)

            response_back = {
                'status_code': status.HTTP_201_CREATED,
                'status_message': "successfully inserted"
            }

            return response_back
        else:
            return status.HTTP_401_UNAUTHORIZED
    else:
        return status.HTTP_400_BAD_REQUEST

def geo_reference_func(payload, additionalFields):
    serializer = GeoReferencePointsSerializer_serializer(data=payload)
    # serializer = Storage_facilitySerializer_serializer(request.data, many=True).data
    if serializer.is_valid(raise_exception=True):
        user = User.objects.get(username=serializer.data['auth_user'])
        if user.check_password(serializer.data['auth_password']):
            user = User.objects.get(username=serializer.data['username'])
            created_by_id = user.id
            # created_by_id = 4

            # queryset = GeoReferencePoints.objects.filter(report_name=serializer.data['report_name'])

            data_save = GeoReferencePoints(
                    comment=serializer.data['comments'],
                    location=serializer.data['location'],
                    created_by_id=created_by_id)

            data_save.save()
            data_save.report_name = formulate_insert_id(13,str(data_save.id))
            data_save.save()

            insert_notification(13,"Geo-reference",data_save.report_name,user)

            response_back = {
                'status_code': status.HTTP_201_CREATED,
                'status_message': "successfully inserted"
            }

            return response_back
        else:
            return status.HTTP_401_UNAUTHORIZED
    else:
        return status.HTTP_400_BAD_REQUEST

def fuel_farm_func(payload, additionalFields):
    serializer = FuelFarmSerializer_serializer(data=payload)
    # serializer = Storage_facilitySerializer_serializer(request.data, many=True).data
    if serializer.is_valid(raise_exception=True):
        user = User.objects.get(username=serializer.data['auth_user'])
        if user.check_password(serializer.data['auth_password']):
            user = User.objects.get(username=serializer.data['username'])
            created_by_id = user.id
            # created_by_id = 4

            # queryset = GeoReferencePoints.objects.filter(report_name=serializer.data['report_name'])

            data_save = FuelFarm(
                    spillage_status=serializer.data['spillage_status'],
                    impervious_status=serializer.data['impervious_status'],
                    comment=serializer.data['comments'],
                    location=serializer.data['location'],
                    created_by_id=created_by_id)

            data_save.save()
            data_save.report_name = formulate_insert_id(14,str(data_save.id))
            data_save.save()

            insert_notification(14,"Fuel Farm",data_save.report_name,user)

            response_back = {
                'status_code': status.HTTP_201_CREATED,
                'status_message': "successfully inserted"
            }

            return response_back
        else:
            return status.HTTP_401_UNAUTHORIZED
    else:
        return status.HTTP_400_BAD_REQUEST

def work_env_compliance_func(payload, additionalFields):
    serializer = WorkEnvComplianceSerializer_serializer(data=payload)
    # serializer = Storage_facilitySerializer_serializer(request.data, many=True).data
    if serializer.is_valid(raise_exception=True):
        user = User.objects.get(username=serializer.data['auth_user'])
        if user.check_password(serializer.data['auth_password']):
            user = User.objects.get(username=serializer.data['username'])
            # created_by_id = user.id
            # created_by_id = 4

            # queryset = GeoReferencePoints.objects.filter(report_name=serializer.data['report_name'])

            data_save = WorkEnvCompliance(
                    first_aid=serializer.data['first_aid'],
                    safety_stickers=serializer.data['safety_stickers'],
                    fire_alarm=serializer.data['fire_alarm'],
                    flooding=serializer.data['flooding'],
                    flammables=serializer.data['flammables'],
                    estinguishers=serializer.data['estinguishers'],
                    no_of_estinquishers=serializer.data['no_of_estinquishers'],
                    comment=serializer.data['comments'],
                    location=serializer.data['location'],
                    created_by=user)

            data_save.save()
            data_save.report_name = formulate_insert_id(15,str(data_save.id))
            data_save.save()

            insert_notification(15,"Work Environment Compliance",data_save.report_name,user)

            response_back = {
                'status_code': status.HTTP_201_CREATED,
                'status_message': "successfully inserted"
            }

            return response_back
        else:
            return status.HTTP_401_UNAUTHORIZED
    else:
        return status.HTTP_400_BAD_REQUEST

def warehouse_func(payload, additionalFields):
    serializer = WarehouseSerializer_serializer(data=payload)
    # serializer = Storage_facilitySerializer_serializer(request.data, many=True).data
    if serializer.is_valid(raise_exception=True):
        user = User.objects.get(username=serializer.data['auth_user'])
        if user.check_password(serializer.data['auth_password']):
            user = User.objects.get(username=serializer.data['username'])
            created_by_id = user.id
            # created_by_id = 4

            # queryset = GeoReferencePoints.objects.filter(report_name=serializer.data['report_name'])

            data_save = Warehouse(
                    eye_wash=serializer.data['eye_wash'],
                    shower=serializer.data['shower'],
                    comment=serializer.data['comments'],
                    location=serializer.data['location'],
                    created_by_id=created_by_id)

            data_save.save()
            data_save.report_name = formulate_insert_id(16,str(data_save.id))
            data_save.save()

            insert_notification(16,"Warehouse",data_save.report_name,user)

            response_back = {
                'status_code': status.HTTP_201_CREATED,
                'status_message': "successfully inserted"
            }

            return response_back
        else:
            return status.HTTP_401_UNAUTHORIZED
    else:
        return status.HTTP_400_BAD_REQUEST

def conveyers_func(payload, additionalFields):
    queryset = WorkEnvCompliance.objects.all()
    serializer = WorkEnvComplianceSerializer_serializer(data=payload)
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
                    comment=serializer.data['comments'],
                    location=serializer.data['location'],
                    created_by_id=created_by_id)

            data_save.save()
            data_save.report_name = formulate_insert_id(17,str(data_save.id))
            data_save.save()

            insert_notification(17,"Conveyers",data_save.report_name,user)

            response_back = {
                'status_code': status.HTTP_201_CREATED,
                'status_message': "successfully inserted"
            }

            return response_back
        else:
            return status.HTTP_401_UNAUTHORIZED
    else:
        return status.HTTP_400_BAD_REQUEST

def incident_report_func(payload, additionalFields):
    serializer = IncidentReportSerializer_serializer(data=payload)
    # serializer = Storage_facilitySerializer_serializer(request.data, many=True).data
    if serializer.is_valid(raise_exception=True):
        user = User.objects.get(username=serializer.data['auth_user'])
        if user.check_password(serializer.data['auth_password']):
            user = User.objects.get(username=serializer.data['username'])
            created_by_id = user.id
            # created_by_id = 4

            # queryset = GeoReferencePoints.objects.filter(report_name=serializer.data['report_name'])

            data_save = IncidentReport(
                    incident_category=serializer.data['incident_category'],
                    incident_location=serializer.data['incident_location'],
                    victim_name=serializer.data['victim_name'],
                    incident_start=serializer.data['incident_start'],
                    incident_end=serializer.data['incident_end'],
                    cause_of_incident=serializer.data['cause_of_incident'],
                    actions_taken_immediately=serializer.data['actions_taken_immediately'],
                    further_actions_taken=serializer.data['further_actions_taken'],
                    corrective_measures=serializer.data['corrective_measures'],
                    responsible_person=serializer.data['responsible_person'],
                    comment=serializer.data['comments'],
                    location=serializer.data['location'],
                    created_by_id=created_by_id)

            data_save.save()
            data_save.report_name = formulate_insert_id(18,str(data_save.id))
            data_save.save()

            insert_notification(18,"Incident Report",data_save.report_name,user)

            response_back = {
                'status_code': status.HTTP_201_CREATED,
                'status_message': "successfully inserted"
            }

            return response_back
        else:
            return status.HTTP_401_UNAUTHORIZED
    else:
        return status.HTTP_400_BAD_REQUEST

def water_management_func(payload, additionalFields):
    # queryset = Energy_management.objects.all()

    logger.info("Additional fields are ")

    logger.info(additionalFields)
    
    serializer = Water_managementSerializer_serializer(data=payload)
    # serializer = Storage_facilitySerializer_serializer(request.data, many=True).data
    if serializer.is_valid(raise_exception=True):
        user = User.objects.get(username=serializer.data['auth_user'])
        if user.check_password(serializer.data['auth_password']):
            serializer.data['report_name'] = "Zip_1"
            user = User.objects.get(username=serializer.data['username'])
            # created_by_id = user.id
            # created_by_id = 4

            data_save = Water_management(
                    total_water_quantity_available=serializer.data['total_water_quantity_available'],
                    camp_consumption=serializer.data['camp_consumption'],
                    admin_consumption=serializer.data['admin_consumption'],
                    cafeteria_consumption=serializer.data['cafeteria_consumption'],
                    workshop_consumption=serializer.data['workshop_consumption'],
                    mine_plant_consumption=serializer.data['mine_plant_consumption'],
                    other_consumption=serializer.data['other_consumption'],
                    comment=serializer.data['comments'],
                    location=serializer.data['location'],
                    created_by=user)

            data_save.save()
            data_save.report_name = formulate_insert_id(15,str(data_save.id))
            data_save.save()

            insert_notification(19,"Water Management",data_save.report_name,user)

            response_back = {
                'status_code': status.HTTP_201_CREATED,
                'status_message': "successfully inserted"
            }

            return response_back
        else:
            return status.HTTP_401_UNAUTHORIZED
    else:
        return status.HTTP_400_BAD_REQUEST

class postRequestViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = formSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            logger.info("data is ")
            # data_json = json.loads(serializer.data['fields'][0])
            logger.info(serializer.data)
            logger.info(serializer.data['fields'])

            logger.info("additional data is ")
            logger.info(serializer.data['additionalFields'])

            additionalFields = serializer.data['additionalFields']

            if additionalFields is None:
                # additionalFields_list = list(additionalFields.split(","))
                additionalFields = []
                # logger.info(additionalFields_list)

            response_m = "incomplete"
            for payload in serializer.data['fields']:
                logger.info("other data is ")
                logger.info(payload)
                # logger.info(payload['additionalFields'][0])

                # Manipulate payload

                #assign authentication variables
                payload['auth_user'] = 'system_user'
                payload['auth_password'] = 'j6d^tUBJ8tS9=URF'

                # check payload
                if payload['location'] == "":
                    payload['location'] = "0,0"
                elif payload['location'] == "null":
                    payload['location'] = "0,0"

                if "username" in payload:
                    pass
                else:
                    payload['username'] = "inputter"

                modulesx = modules.objects.filter(active=1)

                # additionalFields = payload['additionalFields']

                # payload = delattr(payload, "additionalFields")

                for m in modulesx:
                    if m.module_name == serializer.data['module']:
                        #Convert string to function
                        logger.info("module is ")
                        logger.info(m.module_name)
                        func_to_run = globals()[m.module_name+"_func"]
                        response_m = func_to_run(payload, additionalFields)
                    


            # user = User.objects.get(username=serializer.data['auth_user'])
            # if user.check_password(serializer.data['auth_password']):
            queryset = modules.objects.all()

            return Response(response_m,status.HTTP_202_ACCEPTED)
            # else:
            #     return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
