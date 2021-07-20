from django.shortcuts import render
from rest_framework import viewsets
from dataProcessor.serializers import ImageSerializer_serializer
from dataProcessor.serializers import ImageSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from analytics.models import Image

import logging

logger = logging.getLogger("django")


class ImageUploader(viewsets.ViewSet):
    def create(self, request):
        parser_classes = (FormParser, MultiPartParser)
        queryset = Image.objects.all()
        image_serializer = ImageSerializer_serializer(data=request.data)
        # image_model_serializer = ImageSerializer(data=request.data)

        logger.info("Selected images are ")
        logger.info(request.data)

        if image_serializer.is_valid(raise_exception=True):
            user = User.objects.get(username=image_serializer.data['auth_user'])
            if user.check_password(image_serializer.data['auth_password']):
                user = User.objects.get(username=image_serializer.data['username'])
                created_by_id = user.id
                # images = request.FILES.getlist['image']
                image_sav = Image()
                image_sav.module_id = image_serializer.data['module_id']
                image_sav.report_id = image_serializer.data['report_id']
                image_sav.created_by_id = created_by_id
                image_sav.image = request.FILES['image']
                image_sav.save()
    
                return Response(ImageSerializer(image_sav).data, status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        # image_serializer = Storage_facilitySerializer_serializer(request.data, many=True).data
        
        
   
    	
