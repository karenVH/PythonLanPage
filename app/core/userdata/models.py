from django.db import models
from ckeditor.fields import RichTextField
from django.conf import settings

# Create your models here.

class Roles(models.Model):
    roleName = models.CharField(verbose_name="Nombre de Rol", max_length= 50)

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"

    def __str__(self):
        return self.roleName

# Modelo de la entidad Datos de usuario:

class DatosUser(models.Model):
    usuarioid = models.CharField(max_length=20, verbose_name= "Identificación")
    nombuser = models.CharField(max_length=256, verbose_name= "Nombres")
    apeluser = models.CharField(max_length=256, verbose_name= "Apellidos")
    emailuser = models.CharField(max_length=256, verbose_name= "Correo Electrónico")
    fotouser = models.ImageField(upload_to= "img/perfiles", verbose_name= "Imagen de Usuario")
    teleuser = models.CharField(max_length=25, verbose_name= " Teléfono de contácto")
    estauser = models.CharField(max_length=20, default="Activo", verbose_name="Estado")
    creadoel = models.DateTimeField(auto_now_add = True, auto_now=False, verbose_name="Registrado el:")
    modificado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Datos personales"
        verbose_name_plural = "Datos de Usuario"

    def __str__(self):
        return self.nombuser

# Modelo de la entidad habilidades:

class HabilUser(models.Model):
    nombhabil = models.CharField(max_length=45, verbose_name= "Habilidad")

    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades"

    def __str__(self):
        return self.nombhabil

# Modelo de la entidad detalle de roles:
class DetaRoles(models.Model):
    idrol = models.ForeignKey(Roles, on_delete=models.CASCADE, verbose_name="Rol")
    iduser = models.ForeignKey(DatosUser, on_delete=models.CASCADE, verbose_name="Usuario")
    estarol = models.CharField(max_length=50, default="Activo", verbose_name="Status")
    agregado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Detalle de perfil"
        verbose_name_plural = "Perfiles de Usuario"
    
    def __str__(self):
        return self.estarol

# modelo de la entidad rates:

class Rates(models.Model):
    idhabil = models.ForeignKey(HabilUser, on_delete=models.CASCADE, verbose_name= "Habilidad")
    iduser = models.ForeignKey(DatosUser, on_delete=models.CASCADE, verbose_name= "Usuario")
    rate = models.DecimalField(max_digits=3, decimal_places=1, verbose_name= "Calificación")

    class Meta:
        verbose_name = "Rate"
        verbose_name_plural = "Nivel de Habilidad"

    def __unicode__(self):
        return self.rate



