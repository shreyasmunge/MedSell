from django.db import models
from django.contrib.auth.models import AbstractUser
#abstractuser is inbuild model to create user with ease like for ecommerce ,if you want to add more fiels to inbuid User model use this
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15)
    def __str__(self):
        return self.username

class Products(models.Model):
    productname = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/') #to upload image

    def __str__(self):
        return self.productname

#after migration and creating superuser , register your models in admin.py so that you can edit filds from admin