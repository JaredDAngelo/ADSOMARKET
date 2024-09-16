from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class CuentaGerente(BaseUserManager):
    def create_user(self, nombre, apellido, username, correo, ciudad, telefono, password=None):
        if not correo:
            raise ValueError("El usuario debe tener una dirección de correo electrónico")
        
        if not username:
            raise ValueError("El usuario debe tener un nombre de usuario")
        
        usuario = self.model(
            correo = self.normalize_email(correo),
            username = username,
            nombre = nombre,
            apellido = apellido,
            telefono = telefono,
            ciudad = ciudad,
        )

        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, nombre, apellido, correo, username , password):
        usuario = self.create_user(
            correo = self.normalize_email(correo),
            username = username,
            password = password,
            nombre = nombre,
            apellido = apellido,
        )
        usuario.administrador = True
        usuario.activo = True
        usuario.is_staff = True
        usuario.superadministrador = True
        usuario.save(using=self._db)
        return usuario



class Cuenta(AbstractBaseUser):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=100, unique=True)
    ciudad = models.CharField(max_length=50)
    departamento = models.CharField(max_length=100)
    telefono = models.CharField(max_length=50)

    #required
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    ultima_sesion = models.DateTimeField(auto_now_add=True)
    administrador = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    activo = models.BooleanField(default=False)
    superadministrador = models.BooleanField(default=False)

    USERNAME_FIELD = "correo"
    REQUIRED_FIELDS = ['username', 'nombre', 'apellido']

    objects = CuentaGerente()

    def __str__ (self):
        return self.correo
    
    def has_perm (self, perm, obj=None):
        return self.administrador
    
    def has_module_perms (self, add_label):
        return True
