from django.db import models
from django.contrib.auth.models import User

class Producto(models.Model):
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False  # Evita que Django intente crear/modificar esta tabla
        db_table = 'products_product'  # Nombre real de la tabla en MySQL

    def __str__(self):
        return f"Producto {self.id}"

class Mensaje(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.autor.username}: {self.contenido}"
