from django.shortcuts import render
from rest_framework import viewsets
from dataProcessor.serializers import GeoReferencePointsSerializer
from dataProcessor.serializers import GeoReferencePointsSerializer_serializer
from analytics.models import GeoReferencePoints
from analytics.models import Notifications
from analytics.models import NotificationViewer
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status

from dataProcessor.view_controllers.formulateID import formulate_insert_id
from analytics.view_controllers.notifications import insert_notification


class Geo_referenceViewSet(viewsets.ViewSet):
    def create(self, request):
        queryset = GeoReferencePoints.objects.all()

        serializer = GeoReferencePointsSerializer_serializer(data=request.data)
        # serializer = Storage_facilitySerializer_serializer(request.data, many=True).data

        if serializer.is_valid(raise_exception=True):
            user = User.objects.get(username=serializer.data['username'])
            created_by_id = user.id
            # created_by_id = 4

            # queryset = GeoReferencePoints.objects.filter(report_name=serializer.data['report_name'])

            data_save = GeoReferencePoints(
                    comment=serializer.data['comment'],
                    location=serializer.data['location'],
                    created_by_id=created_by_id)

            data_save.save()
            data_save.report_name = formulate_insert_id(13,str(data_save.id))
            data_save.save()

            insert_notification(13,"Geo-reference",data_save.report_name,user)

            return Response(GeoReferencePointsSerializer(data_save).data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)