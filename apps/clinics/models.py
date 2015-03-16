from django.db import models

class Clinic(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=25)
    direccion = models.CharField(verbose_name="Direccion",max_length=40)
    telefono = models.CharField(verbose_name="Telefono",max_length=15)
    correo = models.EmailField(max_length=75)
    foto= models.ImageField(upload_to="clinics/img",blank=True,null=True)
    latitud = models.FloatField()
    longitud = models.FloatField()

    def __unicode__(self):
        return self.nombre
