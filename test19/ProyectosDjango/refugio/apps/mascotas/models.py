from django.db import models
from apps.adopciones.models import Persona
# Create your models here.
class Vacuna (models.Model):
	nombre= models.CharField(max_length=50)

	#############################################
class Mascota(models.Model):
	nombre=models.CharField(max_length=50)
	sexo= models.CharField(max_length=10)
	edad_aproximada=models.IntegerField()
	fecha_rescate=models.DateField()
	Vacuna=models.ManyToManyField(Vacuna, blank=True)



