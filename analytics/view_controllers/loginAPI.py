from django.contrib.auth.models import User
from analytics.serializers import UserSerializer
from analytics.serializers import UsernameSerializer
from analytics.serializers import UserResponseAuth
from rest_framework.views import APIView
from rest_framework import generics

# from django.contrib.auth import authenticate, login as auth_login, logout

from rest_framework.response import Response
from rest_framework import viewsets
from rest_auth.views import LoginView

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import authentication
from rest_framework import exceptions

from django.contrib.auth.hashers import make_password

from rest_framework import status

import logging

logger = logging.getLogger("django")

class loginViewSet_s(APIView):
    def post(self, request):
        # username = request.META.get('HTTP_X_USERNAME')
        serializer = UserSerializer(data=request.data)

        logger.info("data is ")
        logger.info(request.session.session_key)

        response_message = "unsuccessful"

        token = "null"
        status_resp = status.HTTP_400_BAD_REQUEST

        class R_payload: pass

        response_payload = R_payload()

        response_payload.token = token
        response_payload.response_message = response_message
        response_payload.user = ""
        response_payload.response_code = status_resp

        if serializer.is_valid(raise_exception=True):
            username = serializer.data['username']
            password = serializer.data['password']
            # password = make_password(serializer.data['password'])
            # username = request.META.get('username')
            if not username:
                return None

            try:
                user = User.objects.get(username=username)
                response_message = "unsuccessful"

                user_detais = ""

                if user.check_password(password):
                    response_message = "successful"
                    user_detais = UsernameSerializer(user).data
                    token = request.session.session_key
                    status_resp = status.HTTP_202_ACCEPTED

                response_payload.token = token
                response_payload.response_message = response_message
                response_payload.user = user_detais
                response_payload.response_code = status_resp

            except User.DoesNotExist:
                # raise exceptions.AuthenticationFailed('No such user')
                # response_message = "User credentials are incorrect"
                response_message = "unsuccessful"
                response_payload.response_message = response_message

            return Response(UserResponseAuth(response_payload).data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(UserResponseAuth(response_payload).data, status=status.HTTP_400_BAD_REQUEST)


# class loginViewSet(APIView):
#     queryset = User.objects.all()
#     # def post(self, request):
#     # authentication_classes = [SessionAuthentication, BasicAuthentication]
#     # permission_classes = [IsAuthenticated]
#     serializer = UserSerializer(data=request.data)

#     response_message = "Invalid request"

#     if serializer.is_valid(raise_exception=True):
#         logger.info("user data is ")
#         logger.info(serializer.data['username'])
#         logger.info(serializer.data['password'])

#         username = serializer.data['username']
#         password = serializer.data['password']
#         user = authenticate(username=username,password=password)
#         if user is not None:
#             # auth_login(request, user)
#             user = User.objects.get(username=username)
#             if user.is_staff == 1:
#                 response_message = "Unauthorized"
#             else:
#                 response_message = "Successful Authentication"
#         else:
#             response_message = "User does not exist"

#         return Response(response_message, status=status.HTTP_202_ACCEPTED)
#     else:
#         return Response(response_message, status=status.HTTP_400_BAD_REQUEST)


# def create(self, request):
#     serializer = formSerializer(data=request.data)
    
    #     if serializer.is_valid(raise_exception=True):
    #         logger.info("data is ")
    #         # data_json = json.loads(serializer.data['fields'][0])
    #         logger.info(serializer.data['fields'])
    #         response_m = "incomplete"
    #         for payload in serializer.data['fields']:
    #             logger.info("other data is ")
    #             logger.info(payload)
    #              # logger.info(payload['stability_of_dam_walls'])

    #             # Manipulate payload

    #             #assign authentication variables
    #             payload['auth_user'] = 'system_user'
    #             payload['auth_password'] = 'j6d^tUBJ8tS9=URF'

    #             # check payload
    #             if payload['location'] == "":
    #                 payload['location'] = "0,0"

    #             modulesx = modules.objects.filter(active=1)

    #             for m in modulesx:
    #                 logger.info("other data is ")
    #                 logger.info(m.module_name)

    #                 if m.module_name == serializer.data['module']:
    #                     #Convert string to function
    #                     func_to_run = globals()[m.module_name]
    #                     response_m = func_to_run(payload)
               
    #         # user = User.objects.get(username=serializer.data['auth_user'])
    #         # if user.check_password(serializer.data['auth_password']):
    #         queryset = modules.objects.all()

    #         return Response(response_m,status.HTTP_202_ACCEPTED)
    #         # else:
    #         #     return Response(status=status.HTTP_401_UNAUTHORIZED)
    #     else:
    #         return Response(status=status.HTTP_400_BAD_REQUEST)