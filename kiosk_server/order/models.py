from django.db import models
from accounts.models import Membership, CustomUser

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    IsDeleted = models.BooleanField(default=False)
    
    def __str__(self):
        return self.category_name

class Menu(models.Model):
    ID = models.AutoField(primary_key=True, null=False)
    category_ID = models.ForeignKey(Category, on_delete=models.CASCADE)
    owner_ID = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=False)
    image = models.ImageField(upload_to='menu/', null=True)
    price = models.IntegerField(null=False)
    IsDeleted = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    ID = models.AutoField(primary_key=True, null=False)
    Membership_ID = models.ForeignKey(Membership, on_delete=models.CASCADE)
    total_price = models.IntegerField(null=False)
    order_num = models.IntegerField(null=False)
    order_age = models.IntegerField(null=False)
    package = models.BooleanField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    IsDeleted = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'Order'

class Order_amount(models.Model):
    ID = models.AutoField(primary_key=True, null=False)
    menu_ID = models.ForeignKey(Menu, on_delete=models.CASCADE)
    teenager = models.IntegerField(default=0) # 0-2, 4-6, 8-12
    adult = models.IntegerField(default=0) # 15-20, 25-32
    elder = models.IntegerField(default=0) # 38-43, 48-53
    aged = models.IntegerField(default=0) # 60-100
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    IsDeleted = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'Order_amount'
    
        
class Order_menu(models.Model):
    ID = models.AutoField(primary_key=True, null=False)
    Order_ID = models.ForeignKey(Order, on_delete=models.CASCADE)
    Menu_ID = models.ForeignKey(Menu, on_delete=models.CASCADE)
    count = models.IntegerField(null=False)
    
    class Meta:
        db_table = 'Order_menu'

class Options(models.Model):
    ID = models.AutoField(primary_key=True, null=False)
    category_ID = models.ForeignKey(Category, on_delete=models.CASCADE)
    order_menu_ID = models.ForeignKey(Order_menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=False)
    cost = models.IntegerField(null=False)
    IsDeleted = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name