from django.db import models

# Create your models here.

class Osoba(models.Model):
	imie_text = models.CharField(max_length=20)
	nazwisko_text = models.CharField(max_length=20)

	def __str__(self):
	    return self.nazwisko_text+' '+self.imie_text

#class Przedmiot(models.Model):
#	nazwa_przedm = models.CharField(max_length=20, default='NaN')

#	def __str__(self):
#	    return self.nazwa_przedm

class Oceny(models.Model):
	osoba = models.ForeignKey(Osoba)
        nazwa_przedm = models.CharField(max_length=20, default='NaN')
	oceny = [
	    (0, 0), 
	    (1, 1), (2, 2), 
	    (3, 3), (4, 4), 
	    (5, 5), (6, 6)
	]
	ocena_choice = models.IntegerField(choices=oceny, default=0)        

