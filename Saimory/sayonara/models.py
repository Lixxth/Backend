from django.db import models

# Create your models here.

class Product(models.Model):
    #definir campos de la tabla
    product_name = models.CharField(max_length=100, unique=True)
    product_description = models.CharField(max_length=255)
    product_full_cost = models.DecimalField(max_digits=10, decimal_places=2)
    product_is_ofter = models.BooleanField() 
    product_ofter_cost = models.DecimalField(max_digits=10, decimal_places=2)  

    def __str__(self):
        return self.product_name
    


class HistorialCost(models.Model):
    #definir campos de la tabla
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    change_date = models.DateTimeField()
    product_cost = models.DecimalField(max_digits=10, decimal_places=2)

    product_is_offer = models.BooleanField()


    def __str__(self):
        return self.product.product_name + '   ' + self.change_date.strftime('%Y-%m-%d %H:%M') + '   ' + str(self.product_cost)
   

    