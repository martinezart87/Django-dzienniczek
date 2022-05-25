from django.contrib.auth.models import User, Group
from .models import Klasa, Uczen, Przedmiot, Ocena
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = User
        fields = ['url', 'username', 'last_name', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Group
        fields = ['url', 'name']

class KlasaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Klasa
        fields = ['wychowawca', 'nazwa_klasy']

class UczenSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Uczen
        fields = ['klasa', 'imie', 'nazwisko']

class PrzedmiotSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Przedmiot
        fields = ['nazwa']

class OcenaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Ocena
        fields = ['uczen', 'przedmiot', 'ocena']