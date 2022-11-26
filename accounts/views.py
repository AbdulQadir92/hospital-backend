from django.contrib.auth.models import User, auth

from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


# Create your views here.
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
def register(request):
    data = request.data
    username = data['username']
    password1 = data['password1']
    password2 = data['password2']

    if password1 == password2:
        if User.objects.filter(username=username).exists():
            return Response({'message': 'Account with this Phone Number or Email already exists'})
        else:
            User.objects.create_user(username=username, password=password1)
            user = auth.authenticate(username=username, password=password1)
            if user is not None:
                auth.login(request, user)
            else:
                return Response({'message': 'Something went wrong'})

            return Response({'message': 'Account created successfully'})

    else:
        return Response({'message': 'Passwords do not match'})
