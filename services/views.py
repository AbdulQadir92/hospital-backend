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
def add_service(request):
    try:
        title = request.POST.get('title')
        image = request.FILES.get('image')
        p1 = request.POST.get('p1')
        p2 = request.POST.get('p2')
        p3 = request.POST.get('p3')

        if p2 == 'undefined':
            p2 = ''
        if p3 == 'undefined':
            p3 = ''

        service = Service.objects.create(
            title=title, image=image, p1=p1, p2=p2, p3=p3)
        serializer = ServiceSerializer(service, many=False)
        return Response(serializer.data)
    except:
        return Response({'message': 'Something went wrong'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_services(request):
    try:
        services = Service.objects.filter(deleted_at=None)
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)
    except:
        return Response({'message': 'Something went wrong'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_service(request, id):
    try:
        service = Service.objects.get(id=id, deleted_at=None)
        serializer = ServiceSerializer(service, many=False)
        return Response(serializer.data)
    except:
        return Response({'message': 'Something went wrong'})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_service(request, id):
    try:
        title = request.POST.get('title')
        image = request.FILES.get('image')
        p1 = request.POST.get('p1')
        p2 = request.POST.get('p2')
        p3 = request.POST.get('p3')

        service = Service.objects.get(id=id)
        service.updated_by = request.user.id
        service.deleted_at = datetime.datetime.now()

        if image:
            updated_service = Service.objects.create(
                title=title, image=image, p1=p1, p2=p2, p3=p3)
        else:
            updated_service = Service.objects.create(
                title=title, image=service.image, p1=p1, p2=p2, p3=p3)

        service.save()

        serializer = ServiceSerializer(updated_service, many=False)
        return Response(serializer.data)
    except:
        return Response({'message': 'Something went wrong'})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_service(request, id):
    try:
        service = Service.objects.get(id=id)
        service.deleted_by = request.user.id
        service.deleted_at = datetime.datetime.now()
        service.save()

        serializer = ServiceSerializer(service, many=False)
        return Response(serializer.data)
    except:
        return Response({'message': 'Something went wrong'})
