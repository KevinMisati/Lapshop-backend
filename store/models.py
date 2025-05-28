from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.URLField(null=True,blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.URLField(null=True,blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    brand = models.ForeignKey(Brand,related_name='products',on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products',default=1)
    model_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    old_price = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    description = models.TextField()
    stock = models.IntegerField()
    image = models.URLField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    processor = models.CharField(max_length=200, blank=True, null=True)
    ram = models.CharField(max_length=100, blank=True, null=True)
    storage = models.CharField(max_length=100, blank=True, null=True)
    trending = models.BooleanField(default=False)
    mostLoved = models.BooleanField(default=False)


    def save(self,*args,**kwargs):
        if not self.old_price:
            self.old_price = self.price
        super(Product,self).save(*args,**kwargs)

    def __str__(self):
        return f"{self.brand.name} {self.model_name}"