from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework import viewsets
from django.utils.text import slugify

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
from analytics.models import WasteDetails
from analytics.models import Conveyers
from analytics.models import IncidentReport
from analytics.models import Graph_config

from analytics.models import reports

from analytics.serializers import ModulesSerializer
from analytics.serializers import formSerializer

from  analytics.forms import loginForm
from  analytics.forms import indexloginForm
from  analytics.forms import registerForm
from  analytics.forms import editForm

from rest_framework import status

from django.conf import settings

from PIL import Image as PImage

import logging
import os
import shutil

logger = logging.getLogger("django")

import json 


# Create your views here.

def index(request):
    if request.method == 'POST':
        form = loginForm(request.POST)

        if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                user = authenticate(username=username,password=password)

                if user is not None:
                    auth_login(request, user)
                    user = User.objects.get(username=username)

                    if user.is_staff == 1:
                        return HttpResponseRedirect('/analytics/dashboard')
                    else:
                        return HttpResponseRedirect('/dataProcessor/')
                else:
                    return HttpResponseRedirect('login')
    else:
        form = loginForm()
        return render(request, 'analytics/landingpage/index.html',{'form': form})

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'analytics/dashboard/dashboard.html')
    else:
        return HttpResponseRedirect('login')

def documentation(request):
    return render(request, 'analytics/documentation.html')

def admin_documentation(request):
    return render(request, 'analytics/admin_documentation.html')

def inputter_documentation(request):
    return render(request, 'analytics/inputter_documentation.html')

def login(request):
    if request.method == 'POST':
        form = loginForm(request.POST)

        if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                user = authenticate(username=username,password=password)

                if user is not None:
                    auth_login(request, user)
                    user = User.objects.get(username=username)

                    if user.is_staff == 1:
                        return HttpResponseRedirect('/analytics/dashboard')
                    else:
                        return HttpResponseRedirect('/dataProcessor/')
                else:
                    return HttpResponseRedirect('login')
    else:
        form = loginForm()
        return render(request, 'analytics/login/login.html', {'form': form})
	

def registerUser(request):
    if request.method == 'POST':
        form = registerForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password_confirm = form.cleaned_data['password_confirm']
            firstname = form.cleaned_data['first_name']
            lastname = form.cleaned_data['last_name']
            email = form.cleaned_data['email']

            if  password != password_confirm:
                 return render(request, 'analytics/login/register.html', {
                    'form': form,
                    'error_message': ' Passwords do not match '
                })

            else:
                user = User.objects.create_user(username, email, password)
                user.last_name = lastname
                user.first_name = firstname
                user.save()

                return HttpResponseRedirect('register_user')
    else:
        form = registerForm()
        return render(request, 'analytics/login/register.html',{'form': form})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('login')

def media(request):
    if request.user.is_authenticated:
        modules_queryset = modules.objects.filter(active=1)
        
        media_directories = os.listdir(settings.MEDIA_ROOT)
        image_queryset = []

        logger.info("Media folders are ")
        logger.info(settings.MEDIA_ROOT)
        logger.info(os.listdir(settings.MEDIA_ROOT))

        if request.method == 'POST':
            logger.info("Media files are ")
            logger.info(request.POST['folder'])

            path = os.path.join('media',slugify(request.POST['folder']))
            imagesList = os.listdir(path)


            for image_r in imagesList:
                class image:
                    class image:
                        url = ""

                path = os.path.join(path, image_r)
                logger.info(image_r)
                image.image.url = "/"+path
                # img = PImage.open(path)
                # This is appending each image path which should not be so
                logger.info("path is ")
                logger.info(image.image.url)
                logger.info(image)
                image_queryset.append(image)

                # Attempted destroying the object but for some reason it is still appended
                del image

            logger.info(image_queryset)
        else:
            image_queryset = Image.objects.select_related('module')
        return render(request, 'analytics/dashboard/media.html',{'modules':modules_queryset,'images':image_queryset,'directories':media_directories})
    else:
        return HttpResponseRedirect('login')

def add_folder(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            path = os.path.join('media',slugify(request.POST['folder_name']))
            try:
                os.mkdir(path)
            except OSError:
                pass

        return HttpResponseRedirect('media')

    else:
        return HttpResponseRedirect('login')

def add_to_folder(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            logger.info("Selected images are ")
            logger.info(request.POST['selected_images'])
            selected_images = request.POST['selected_images'].split(",")
            folder_to_move_file_into = request.POST['folder_name']

            destination_path = os.path.join(settings.MEDIA_ROOT,slugify(request.POST['folder_name']))

            logger.info(selected_images)
            logger.info(" and path ")
            logger.info(destination_path)
            queryset = Image.objects.filter(id__in=selected_images)

            for value in queryset:
                logger.info(value)
                source_path = os.path.join(settings.MEDIA_ROOT,value.image.name)
                shutil.copy(source_path, destination_path)

            logger.info(queryset)

        return HttpResponseRedirect('media')
    else:
        return HttpResponseRedirect('login')

def delete_images(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            selected_images = request.POST['selected_images'].split(",")
            Image.objects.filter(id__in=selected_images).delete()
        return HttpResponseRedirect('media')
    else:
        return HttpResponseRedirect('login')

def graph_builder(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            chart_type = request.POST['chart']
            module_id = request.POST['module']
            x_axis = request.POST['x-axis']
            y_axis = request.POST['y-axis']
            graph_name = request.POST['graph_name']
            description = request.POST['description']

            if 'predictive' in request.POST:
                predictive = request.POST['predictive']
            else:
                predictive = 0

            create_graph = Graph_config(
                graph_name=graph_name,
                graph_type=chart_type, 
                description=description,
                x_column=x_axis, 
                y_column=y_axis, 
                predictive=predictive,
                module_id=module_id,
                created_by_id=request.user.id,
                active=1
                )
            create_graph.save()
            return render(request, 'analytics/dashboard/graph_builder.html')
        else:
            return render(request, 'analytics/dashboard/graph_builder.html')
    else:
        return HttpResponseRedirect('login')

def report_builder(request):
    queryset = reports.objects.all()

    querysetm = modules.objects.filter(active=1)

    return render(request, 'analytics/dashboard/report_builder.html',
        {
            'data':queryset,
            'modules':querysetm})

def table_builder(request):
    if request.user.is_authenticated:
        return render(request, 'analytics/dashboard/table_builder.html')
    else:
        return HttpResponseRedirect('login')

def adduser(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = registerForm(request.POST)
    
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                password_confirm = form.cleaned_data['password_confirm']
                firstname = form.cleaned_data['first_name']
                lastname = form.cleaned_data['last_name']
                email = form.cleaned_data['email']
    
                if  password != password_confirm:
                     return render(request, 'analytics/dashboard/adduser.html', {
                        'form': form,
                        'error_message': ' Passwords do not match '
                    })
    
                else:
                    user = User.objects.create_user(username, email, password)
                    user.last_name = lastname
                    user.first_name = firstname
                    user.save()
    
                    return HttpResponseRedirect('add-user')
        else:
            form = registerForm()
            return render(request, 'analytics/dashboard/adduser.html',{'form': form})
    else:
        return HttpResponseRedirect('login')

def edituser(request):
    if request.user.is_authenticated:
        users = User.objects.filter(is_active=1)
        if request.method == 'POST':
            form = editForm(request.POST)

            username = request.POST['username']

            logger.info("username is ")
            logger.info(username)
    
            if form.is_valid():
                logger.info("form is valid ")
                firstname = form.cleaned_data['first_name']
                lastname = form.cleaned_data['last_name']
                email = form.cleaned_data['email']
    
                user = User.objects.get(username=username)
                user.last_name = lastname
                user.first_name = firstname
                user.email = email
                user.save()

                logger.info("email is ")
                logger.info(user.email)
            return render(request, 'analytics/dashboard/edituser.html',{'form': form,'users':users})
        else:
            form = editForm()
            return render(request, 'analytics/dashboard/edituser.html',{'form': form,'users':users})
    else:
        return HttpResponseRedirect('login')

def add_report(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            report_name = request.POST['report_name']

            reports_save = reports(
                            report_name=report_name,
                            report_structure="["+report_name+"]",
                            active=1,
                            created_by=request.user
                )
            reports_save.save()

        return HttpResponseRedirect('reports')

    return HttpResponseRedirect('login')


class getModulesViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        # queryset = modules.objects.values('module_name')
        queryset = modules.objects.all()

        return Response(ModulesSerializer(queryset, many=True).data,status.HTTP_202_ACCEPTED)
        # return Response(queryset,status.HTTP_202_ACCEPTED)
        # serializer = ModulesSerializer(data=request.data)

class postRequestViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = formSerializer(data=request.data)

        

        if serializer.is_valid(raise_exception=True):
            logger.info("data is ")
            # data_json = json.loads(serializer.data['fields'][0])
            logger.info(serializer.data['fields'][0]['DamStabilty'])
            # user = User.objects.get(username=serializer.data['auth_user'])
            # if user.check_password(serializer.data['auth_password']):
            queryset = modules.objects.all()
            return Response(serializer.data,status.HTTP_202_ACCEPTED)
            # else:
            #     return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)




