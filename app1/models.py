from django.db import models
class tbl_RestaurantAccount(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    Restaurantname=models.CharField(max_length=30)
    location=models.CharField(max_length=30)
    typeofshop=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    phone=models.IntegerField()
    no_ofstaff=models.IntegerField()
    auth_person=models.CharField(max_length=30)
    p_email=models.EmailField(max_length=30)
    p_contact=models.IntegerField()
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    type=models.CharField(max_length=30)
    class Meta:
        db_table="tbl_RestaurantAccount"

class tbl_UserAccount(models.Model):
    username=models.CharField(max_length=30)
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    gender=models.CharField(max_length=30)
    phone=models.IntegerField()
    email=models.CharField(max_length=30)
    address=models.EmailField(max_length=30)
    district=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    type=models.CharField(max_length=30)
    class Meta:
        db_table="tbl_UserAccount"   

class tbl_feedback(models.Model):
    f_id=models.IntegerField()
    customer_id=models.IntegerField()
    Restaurantname=models.CharField(max_length=30)
    feedback=models.CharField(max_length=30)
    status=models.CharField(max_length=30)
    type=models.CharField(max_length=30)
    class Meta:
        db_table="tbl_feedback"        

class tbl_RestAdmin(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    restname=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    Rest_id=models.CharField(max_length=30)
    type=models.CharField(max_length=30)
    class Meta:
        db_table="tbl_RestAdmin" 
class tbl_FoodMenu(models.Model):
    restname=models.CharField(max_length=30)
    MenuName=models.CharField(max_length=30)
    type=models.CharField(max_length=30)
    cusine=models.CharField(max_length=30)
    origin=models.CharField(max_length=30)
    
    type=models.CharField(max_length=30)
    class Meta:
        db_table="tbl_FoodMenu" 

class Fooditem(models.Model):
    RestaurantName=models.CharField(max_length=30)
    MenuName=models.CharField(max_length=30)
    MenuItemName=models.CharField(max_length=30)
    Quantity=models.IntegerField()
    price=models.IntegerField()
    cookingtime=models.CharField(max_length=30)
    status=models.CharField(max_length=30)
    type=models.CharField(max_length=30)
    class Meta:
        db_table="Fooditem"    

class Offer(models.Model):
    Res_id=models.CharField(max_length=30)
    MenuItemName=models.CharField(max_length=30)
    offer=models.CharField(max_length=30)
    startdate=models.CharField(max_length=30)
    enddate=models.CharField(max_length=30)
    details=models.CharField(max_length=30)
    status=models.CharField(max_length=30)
    type=models.CharField(max_length=30)
    class Meta:
        db_table="Offer"  
class tbl_cart(models.Model):
    username=models.CharField(max_length=30)        
    restname=models.CharField(max_length=30)   
    fooditemname=models.CharField(max_length=30)
    quantity=models.IntegerField() 
    price=models.IntegerField()   
    status=models.CharField(max_length=30)  
    totalprice=models.IntegerField() 
    class Meta:
        db_table="tbl_cart" 
class tbl_order(models.Model):
    username=models.CharField(max_length=30)        
    restname=models.CharField(max_length=30)   
    totalprice=models.IntegerField()
    paymentmode=models.CharField(max_length=30) 
    status=models.CharField(max_length=30)   
    class Meta:
        db_table="tbl_order"               

# Create your models here.
