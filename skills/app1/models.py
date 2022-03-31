from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=128, verbose_name='Nombre del libro')
    isbn = models.IntegerField(default=0, verbose_name='ISBN')
    publisher_date = models.DateField(verbose_name='Fecha publicación')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')

    class Meta:
        db_table = 'books'