from django.db import models

# Create your models here.
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='Category name')
    description = models.TextField(**NULLABLE, verbose_name='Description')


    def __str__(self):
        return f'{self.name}'


    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('pk',)


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='Product name')
    description = models.TextField(**NULLABLE, verbose_name='Description')
    photo = models.ImageField(upload_to='products/', **NULLABLE, verbose_name='Picture')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category name')
    price = models.FloatField(**NULLABLE, verbose_name='Product price')
    date_creation = models.DateField(auto_now=False, auto_now_add=True, verbose_name='Creating date')
    date_changing = models.DateField(auto_now=True, auto_now_add=False, verbose_name='Last changing date')
    def __str__(self):
        return f'{self.name} ({self.category})'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'