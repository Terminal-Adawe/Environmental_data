from django.shortcuts import render
from rest_framework import viewsets
from dataProcessor.serializers import Liquid_waste_oilSerializer
from dataProcessor.serializers import Liquid_waste_oilSerializer_serializer
from analytics.models import Liquid_waste_oil
from analytics.models import Notifications
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status

from dataProcessor.view_controllers.formulateID import formulate_insert_id
from analytics.view_controllers.notifications import insert_notification


class liquid_waste_oilViewSet(viewsets.ViewSet):
    def create(self, request):
        queryset = Liquid_waste_oil.objects.all()

        serializer = Liquid_waste_oilSerializer_serializer(data=request.data)
        # serializer = Storage_facilitySerializer_serializer(request.data, many=True).data

        if serializer.is_valid(raise_exception=True):
            serializer.data['report_name'] = "Zip_1"
            user = User.objects.get(username=serializer.data['username'])
            created_by_id = user.id
            # created_by_id = 4

            data_save = Liquid_waste_oil(
                    discharge_point=serializer.data['discharge_point'],
                    source=serializer.data['source'],
                    comment=serializer.data['comment'],
                    location=serializer.data['location'],
                    created_by_id=created_by_id)

            data_save.save()
            data_save.report_name = formulate_insert_id(15,str(data_save.id))
            data_save.save()
            
            insert_notification(5,"Liquid Waste Oil",data_save.report_name,user)

            return Response(Liquid_waste_oilSerializer(data_save).data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)