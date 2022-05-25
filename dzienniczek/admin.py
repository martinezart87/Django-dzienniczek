from django.contrib import admin
from django.forms import inlineformset_factory
from .models import Klasa, Uczen, Przedmiot, Ocena

admin.site.register([Klasa, Uczen, Przedmiot, Ocena])