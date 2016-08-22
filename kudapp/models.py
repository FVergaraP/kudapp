from __future__ import unicode_literals

from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    def __unicode__(self):
        return self.nombre

class Comuna(models.Model):
    nombre = models.CharField(max_length=50)
    def __unicode__(self):
        return self.nombre

class TipoServicio(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    def __unicode__(self):
        return self.nombre
    categoria = models.ManyToManyField(Categoria)

class Evento(models.Model):
    nombre = models.CharField(max_length=75)
    descripcion = models.TextField()
    fecha_evento = models.DateTimeField()
    pagina_web = models.CharField(max_length=100)
    pagina_facebook = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    comuna = models.ForeignKey(Comuna)
    def __unicode__(self):
        return self.nombre

class User(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo_electronico = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    rut = models.CharField(max_length=10)
    direccion = models.CharField(max_length=100)
    celular = models.CharField(max_length=12)
    fono = models.CharField(max_length=12)
    comuna = models.ForeignKey(Comuna)
    ofrece_servicio = models.BooleanField(default=False)
    cantidad_reportes = models.IntegerField(default=0)
    fecha_registro = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.nombre

class Servicio(models.Model):
    user = models.ForeignKey(User)
    tipo_servicio = models.ForeignKey(TipoServicio)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.IntegerField()
    trabajo_visita = models.BooleanField()
    recibe_efectivo = models.BooleanField()
    recibe_transferencia = models.BooleanField()
    def __unicode__(self):
        return self.titulo


class Comentario(models.Model):
    user = models.ForeignKey(User)
    servicio = models.ForeignKey(Servicio)
    comentario = models.TextField()
    def __unicode__(self):
        return self.comentario

class Calificacion(models.Model):
    user = models.ForeignKey(User)
    servicio = models.ForeignKey(Servicio)
    calificacion = models.FloatField(default=0)
    def __unicode__(self):
        return self.calificacion










# Create your models here.
