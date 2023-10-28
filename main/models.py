from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()





class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    count = models.IntegerField(default=0)


class Images(models.Model):
    img = models.ImageField(upload_to='pics')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Categories(models.Model):
    name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)



class Brands(models.Model):
    brand_name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Color(models.Model):
    color_type = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class ShoppingCart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_at = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.product.name} from {self.user.name}'


class ShoppingHistory(models.Model):
    STATUS = (
        (1, 'Created'),
        (2, 'Wait for payment'),
        (3, 'Paid'),
        (4, 'Deliverning'),
        (5, 'Completed')
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS)
    count = models.IntegerField(default=1)
    upload_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.product.name} >>>>>>>>> {self.status[1]}'


class DeliveryAddresOfUser(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    CompanyName=models.CharField(max_length=150)
    PhoneNumber=models.CharField(25)
    EmailAddres=models.CharField(max_length=150)
    Country=models.CharField(max_length=150)
    AddressLine1=models.CharField(max_length=150)
    AddressLine2=models.CharField(max_length=150)
    City=models.CharField(max_length=150)
    District=models.CharField(max_length=150)
    Postcode=models.CharField(max_length=150)
    ShippingDetails=models.TextField(max_length=500, default=0)
    date=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.user.name}'


class UserBlogComments(models.Model):
    title = models.CharField(max_length=100)
    comment = models.CharField(max_length=250)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)



class BlogPhotos(models.Model):
    photo = models.ImageField(upload_to='blog_img')
    author = models.ForeignKey(UserBlogComments, on_delete=models.CASCADE, blank=True, null=True)


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    title = models.CharField(max_length=250)
    comment = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
