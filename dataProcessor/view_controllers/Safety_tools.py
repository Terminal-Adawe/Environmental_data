from django.shortcuts import render
from rest_framework import viewsets
from dataProcessor.serializers import Safety_toolsSerializer
from dataProcessor.serializers import Safety_toolsSerializer_serializer
from analytics.models import Safety_tools
from rest_framework.response import Response
from django.contrib.auth.models import User


class Safety_toolsViewSet(viewsets.ViewSet):
    def create(self, request):
        queryset = Safety_tools.objects.all()

        serializer = Safety_toolsSerializer_serializer(data=request.data)
        # serializer = Storage_facilitySerializer_serializer(request.data, many=True).data

        if serializer.is_valid(raise_exception=True):
            serializer.data['report_name'] = "Zip_1"
            user = User.objects.get(username=serializer.data['username'])
            created_by_id = user.id
            # created_by_id = 4

            queryset = Safety_tools.objects.filter(report_name=serializer.data['report_name'])

            status_code = 500
            outData = queryset

            if queryset.exists():
                return Response(Safety_toolsSerializer(outData).data, status=status_code)
            else:
                gah_sav = Safety_tools(
                    report_name=serializer.data['report_name'],
                    no_of_estinquishers=serializer.data['no_of_estinquishers'],
                    fire_alarm=serializer.data['fire_alarm'],
                    status_of_estinguishers=serializer.data['status_of_estinguishers'],
                    comment=serializer.data['comment'],
                    created_by_id=created_by_id)

                gah_sav.save()
                status_code= 200
                outData = gah_sav

            return Response(Safety_toolsSerializer(outData).data, status=status_code)
        else:
            return Response(status=201)