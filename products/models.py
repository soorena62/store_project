from django.db import models

# Create your models here:


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    description = models.TextField()
    cover = models.ImageField()

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
