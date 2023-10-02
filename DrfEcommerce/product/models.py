from django.db import models
from  mptt.models import TreeForeignKey,MPTTModel

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) :
        return self.name

class Category(MPTTModel):
    name = models.CharField(max_length=100)
    parent = TreeForeignKey('self',on_delete=models.CASCADE,null=True,blank=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    is_digital = models.BooleanField(default=True)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    category = TreeForeignKey(Category,on_delete=models.PROTECT)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name  


class ProductLine(models.Model):
    price = models.IntegerField(default=0)
    stoke_qty = models.IntegerField()
    sku= models.CharField(max_length=100)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product_lines")
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.sku

