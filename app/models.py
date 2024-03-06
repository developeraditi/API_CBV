from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    product_cate_id =models.IntegerField(primary_key=True)
    product_cate_name=models.CharField(max_length=100)

    def __str__ (self):
        return self.product_cate_name


class Product(models.Model):
    Product_Id =models.ForeignKey(ProductCategory,on_delete=models.CASCADE)
    Product_Name = models.CharField(max_length=100)
    Product_Price = models.IntegerField()
    Product_Brand =models.CharField(max_length=100)

    def __str__ (self):
        return self.Product_Name

