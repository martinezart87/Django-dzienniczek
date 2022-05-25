from datetime import datetime
from pyexpat import model
from tabnanny import verbose
from django.db import models

class Klasa(models.Model):
    wychowawca = models.CharField(max_length=400)
    nazwa_klasy = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.wychowawca} - {self.nazwa_klasy}' 
    
    class Meta:
        verbose_name="Klasa"
        verbose_name_plural="Klasy"

class Uczen(models.Model):
    klasa = models.ForeignKey(Klasa,on_delete=models.CASCADE)
    imie = models.CharField(max_length=400)
    nazwisko = models.CharField(max_length=400)

    def __str__(self):
        return f'{self.imie} {self.nazwisko} - {self.klasa}'

    class Meta:
        verbose_name="Uczeń"
        verbose_name_plural="Uczniowie"
        ordering= ("nazwisko",)

class Przedmiot(models.Model):
    nazwa = models.CharField(max_length=400)

    def __str__(self):
        return f'{self.nazwa}'

    class Meta:
        verbose_name="Przedmiot"
        verbose_name_plural="Przedmioty"

class Ocena(models.Model):
    uczen = models.ForeignKey(Uczen,on_delete=models.CASCADE)
    przedmiot = models.ForeignKey(Przedmiot,on_delete=models.CASCADE)
    ocena = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.uczen} {self.przedmiot} {self.ocena}'

    class Meta:
        verbose_name="Ocena"
        verbose_name_plural="Oceny"