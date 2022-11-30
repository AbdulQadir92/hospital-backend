from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
import json

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

import datetime


# # Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_appointment(request):
    try:
        data = json.loads(request.body)
        name = data['name']
        email = data['email']
        try:
            service = data['service']
        except:
            service = ''
        doctor = data['doctor']
        date = data['date']
        time = data['time']

        appointment = Appointment.objects.create(
            name=name, email=email, service=service, doctor=doctor, date=date, time=time)
        serializer = AppointmentSerializer(appointment, many=False)
        return Response(serializer.data)
    except:
        return Response({'message': 'Something went wrong'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_appointments(request):
    try:
        appointments = Appointment.objects.filter(deleted_at=None)
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)
    except:
        return Response({'message': 'Something went wrong'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_appointment(request, id):
    try:
        appointment = Appointment.objects.get(id=id, deleted_at=None)
        serializer = AppointmentSerializer(appointment, many=False)
        return Response(serializer.data)
    except:
        return Response({'message': 'Something went wrong'})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_appointment(request, id):
    try:
        data = json.loads(request.body)
        name = data['name']
        email = data['email']
        try:
            service = data['service']
        except:
            service = ''
        doctor = data['doctor']
        date = data['date']
        time = data['time']

        appointment = Appointment.objects.get(id=id)
        appointment.updated_by = request.user.id
        appointment.deleted_at = datetime.datetime.now()
        appointment.save()

        updated_appointment = Appointment.objects.create(
            name=name, email=email, service=service, doctor=doctor, date=date, time=time)
        serializer = AppointmentSerializer(updated_appointment, many=False)
        return Response(serializer.data)
    except:
        return Response({'message': 'Something went wrong'})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_appointment(request, id):
    try:
        appointment = Appointment.objects.get(id=id)
        appointment.deleted_by = request.user.id
        appointment.deleted_at = datetime.datetime.now()
        appointment.save()

        serializer = AppointmentSerializer(appointment, many=False)
        return Response(serializer.data)
    except:
        return Response({'message': 'Something went wrong'})
