from django.shortcuts import render
from rest_framework import viewsets
from dataProcessor.serializers import IncidentReportSerializer
from dataProcessor.serializers import IncidentReportSerializer_serializer
from analytics.models import IncidentReport
from analytics.models import Notifications
from analytics.models import NotificationViewer
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status

from dataProcessor.view_controllers.formulateID import formulate_insert_id
from analytics.view_controllers.notifications import insert_notification


class IncidentReportViewSet(viewsets.ViewSet):
    def create(self, request):
        queryset = IncidentReport.objects.all()

        serializer = IncidentReportSerializer_serializer(data=request.data)
        # serializer = Storage_facilitySerializer_serializer(request.data, many=True).data

        if serializer.is_valid(raise_exception=True):
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
                    comment=serializer.data['comment'],
                    location=serializer.data['location'],
                    created_by_id=created_by_id)

            data_save.save()
            data_save.report_name = formulate_insert_id(18,str(data_save.id))
            data_save.save()

            insert_notification(18,"Incident Report",data_save.report_name,user)

            return Response(IncidentReportSerializer(data_save).data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)