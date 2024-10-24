from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Laptop(models.Model):
    brand = models.ForeignKey(Brand,related_name='laptops',on_delete=models.CASCADE)
    model_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    old_price = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    description = models.TextField()
    stock = models.IntegerField()
    image = models.URLField(null=True,blank=True)#models.ImageField(upload_to='laptops/',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    processor = models.CharField(max_length=200, blank=True, null=True)
    ram = models.CharField(max_length=100, blank=True, null=True)
    storage = models.CharField(max_length=100, blank=True, null=True)
    trending = models.BooleanField(default=False)

    def save(self,*args,**kwargs):
        if not self.old_price:
            self.old_price = self.price
        super(Laptop,self).save(*args,**kwargs)

    def __str__(self):
        return f"{self.brand.name} {self.model_name}"