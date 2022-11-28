from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
import json

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

import datetime


# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_doctor(request):
    try:
        name = request.POST.get('name')
        image = request.FILES.get('image')
        designation = request.POST.get('designation')
        description = request.POST.get('description')

        service = Doctor.objects.create(
            name=name, image=image, designation=designation, description=description)
        serializer = DoctorSerializer(service, many=False)
        return Response(serializer.data)
    except:
        return Response({'message': 'Something went wrong'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_doctors(request):
    try:
        doctors = Doctor.objects.filter(deleted_at=None)
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)
    except:
        return Response({'message': 'Something went wrong'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_doctor(request, id):
    try:
        doctor = Doctor.objects.get(id=id, deleted_at=None)
        serializer = DoctorSerializer(doctor, many=False)
        return Response(serializer.data)
    except:
        return Response({'message': 'Something went wrong'})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_doctor(request, id):
    try:
        name = request.POST.get('name')
        image = request.FILES.get('image')
        designation = request.POST.get('designation')
        description = request.POST.get('description')

        doctor = Doctor.objects.get(id=id)
        doctor.updated_by = request.user.id
        doctor.deleted_at = datetime.datetime.now()

        if image:
            updated_doctor = Doctor.objects.create(
                name=name, image=image, designation=designation, description=description)
        else:
            updated_doctor = Doctor.objects.create(
                name=name, image=doctor.image, designation=designation, description=description)

        doctor.save()

        serializer = DoctorSerializer(updated_doctor, many=False)
        return Response(serializer.data)
    except:
        return Response({'message': 'Something went wrong'})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_doctor(request, id):
    try:
        doctor = Doctor.objects.get(id=id)
        doctor.deleted_by = request.user.id
        doctor.deleted_at = datetime.datetime.now()
        doctor.save()

        serializer = DoctorSerializer(doctor, many=False)
        return Response(serializer.data)
    except:
        return Response({'message': 'Something went wrong'})
