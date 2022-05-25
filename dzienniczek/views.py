from django.contrib.auth.models import User, Group
from .models import Klasa, Uczen, Przedmiot, Ocena
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, GroupSerializer, KlasaSerializer, UczenSerializer, PrzedmiotSerializer, OcenaSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permision_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permision_classes = [permissions.IsAuthenticated]

class KlasaViewSet(viewsets.ModelViewSet):
    queryset = Klasa.objects.all()
    serializer_class = KlasaSerializer
    permision_classes = [permissions.IsAuthenticated]

class UczenViewSet(viewsets.ModelViewSet):
    queryset = Uczen.objects.all()
    serializer_class = UczenSerializer
    permision_classes = [permissions.IsAuthenticated]

class PrzedmiotViewSet(viewsets.ModelViewSet):
    queryset = Przedmiot.objects.all()
    serializer_class = PrzedmiotSerializer
    permision_classes = [permissions.IsAuthenticated]

class OcenaViewSet(viewsets.ModelViewSet):
    queryset = Ocena.objects.all()
    serializer_class = OcenaSerializer
    permision_classes = [permissions.IsAuthenticated]