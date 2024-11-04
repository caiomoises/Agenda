from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

'''
id (primary key - automático)
coisas que irei usar para os contatos: 
firrst_name (string), last_name (string), phone (string),
email (email), created_date (date), description (text)

category (foreign key), show (boolean), owner (foreing key),
picture (imagem).
'''

class Category(models.Model): # Criando as categorias para os contatos
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(
        max_length=50,
        verbose_name='Nome',
    )

    def __str__(self) -> str:
        return self.name

class Contact(models.Model): # Criando contatos
    first_name = models.CharField(
        max_length=50, 
        verbose_name='Primeiro Nome',
    )

    last_name = models.CharField(
        max_length=50, 
        blank=True,
        verbose_name='Último Nome',
    )

    phone = models.CharField(
        max_length=15,
        verbose_name='Telefone',
    )

    email = models.EmailField(
        max_length=254, 
        blank=True,
        verbose_name='E-mail',
    )

    created_date = models.DateTimeField(
        default=timezone.now,
        verbose_name='Data de Criação',
    )

    description = models.TextField(
        blank=True,
        verbose_name='Descrição',
    )

    show = models.BooleanField(
        default=True,
        verbose_name='Mostrar',
    )

    picture = models.ImageField(
        blank=True, 
        upload_to='pictures/%Y/%m/',
        verbose_name='Imagem',
    )
    
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL, 
        blank=True, null=True,
        verbose_name='Categoria',
    )
    
    owner = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        blank=True, null=True,
        verbose_name='Dono',
    )

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'