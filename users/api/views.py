from django.http import JsonResponse, HttpResponse
from .serializer import ClientSerialzer, TrainerSerialzer, RegularSerialzer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.renderers import JSONRenderer
from django.shortcuts import render

from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@authentication_classes((SessionAuthentication, ))
@permission_classes((IsAuthenticated, ))
def api_get_trainees(request, format=None):
    if request.method == 'GET':
        try:
            trainer = request.user.traineraccount
            serialized_data = ClientSerialzer(trainer).data
            return JsonResponse(serialized_data);
        except ObjectDoesNotExist:
            return HttpResponse('Forbidden', status=403)
    return HttpResponse('Unauthorized', status=401)


@api_view(['GET'])
@authentication_classes((SessionAuthentication, ))
@permission_classes((IsAuthenticated, ))
def api_get_user(request, format=None):
    if request.method == 'GET':
        current_user = request.user
        try:
            regular_user = current_user.regularaccount
            serialized_data = RegularSerialzer(regular_user).data
            return JsonResponse(serialized_data)
        except ObjectDoesNotExist:
            pass
        try:
            trainer_user = current_user.traineraccount
            serialized_data = TrainerSerialzer(trainer_user).data
            return JsonResponse(serialized_data)
        except ObjectDoesNotExist:
            return HttpResponse('Unauthorized', status=401)
        return HttpResponse('Unauthorized', status=401)
    return HttpResponse('Unauthorized', status=401)
