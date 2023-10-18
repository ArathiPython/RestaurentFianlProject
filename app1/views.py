from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password,check_password
from django.conf import settings
from app1.models import tbl_RestaurantAccount
from app1.models import tbl_feedback
from app1.models import tbl_FoodMenu
from app1.models import tbl_RestAdmin
from app1.models import tbl_UserAccount
from app1.models import Offer
from app1.models import Fooditem
from app1.models import tbl_cart
from app1.models import tbl_order
def index(request):
    return render(request,"index.html")

#__________________________LOGIN_________________________________________________________________
def log1(request):
    return render(request,"loginForm.html")

def gouser1(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    print(username,password,"test1 auth")
    a1= authenticate(username=username,password=password)
    request.session['username']=username
    print(a1,"test2 auth")

    if a1 is not None and a1.is_superuser ==1:
       return redirect('/a_home/')
    #    data=User.objects.get(username=username)
    #    return render(request,"admin.html",{'data':data})

    elif a1 is not None and a1.is_superuser ==0:
        data=tbl_UserAccount.objects.get(username=username) 
        print(data.type,"test2 auth")
        if data is not None and  data.type=="user": #CHECKING BY TYPE USER
            return redirect('/u_home/')
        elif data is not None and  data.type=="RestAdmin":#CHECKING BY TYPE REST ADMIN
            return redirect('/r_home/')
            # return render(request,"restaurant.html",{"data":data})
    else:
       return HttpResponse("user does not exist")
def logout(request):
    del  request.session['username']
    return redirect('/')
def u_home(request):
    a1= request.session['username']
    print(a1,"text")
    print("text")
    p1=tbl_UserAccount.objects.get(username=a1)
    return render(request,"user.html",{"data":p1}) 
def a_home(request):
    a1= request.session['username']
    print(a1,"text")
    print("text")
    p1=User.objects.get(username=a1)
    return render(request,"admin.html",{"data":p1}) 
def out(request):
    del request.session['username']
    return redirect('/')
def r_home(request):
    a1=request.session['username']
    print(a1,"text")
    print("text")
    p1=tbl_RestaurantAccount.objects.get(username=a1)
    return render(request,"restaurant.html",{'data':p1})
def homee(request):
    return redirect('/index/')
#_________________________________ end Login__________________________________    
    


def create1(request):
    return render(request,"userAccount.html")
def create2(request):
    if request.method =='POST':
         P1=User()
         p2=tbl_UserAccount()
         P1.username=request.POST.get('username')
         password=request.POST.get('password')
         P1.set_password(password)
         P1.first_name=request.POST.get('firstname')
         P1.last_name=request.POST.get('lastname')
         P1.email=request.POST.get('email')

         p2.username=request.POST.get('username')
         p2.firstname=request.POST.get('firstname')
         p2.lastname=request.POST.get('lastname')
         p2.gender=request.POST.get('gender')
         p2.phone=request.POST.get('phone')
         p2.email=request.POST.get('email')
         p2.address=request.POST.get('address')
         p2.district=request.POST.get('district')
         p2.state=request.POST.get('state')
         p2.type="user"
         p2.save()
         P1.save()
         return redirect('/')
def addres1(request):
    a1=request.session['username']
    p1=User.objects.get(username=a1)
    return render(request,"addrestaurant.html",{'data':p1})
def rest1(request):
     p=User()
     p1=tbl_RestaurantAccount()
     p2=tbl_UserAccount()

     p.username=request.POST.get('username')
     password=request.POST.get('password')
     p.set_password(password)
     p.first_name=request.POST.get('firstname')
     p.last_name=request.POST.get('lastname')
     p.email=request.POST.get('email')
    
     
     p2.firstname=request.POST.get('firstname')
     p2.lastname=request.POST.get('lastname')
     p2.gender="None"
     p2.phone=request.POST.get('phone')
     p2.email=request.POST.get('email')
     p2.address=request.POST.get('location')
     p2.district=request.POST.get('location')
     p2.username=request.POST.get('username')
     p2.state="Kerala"
    #  p2.type="user" #?????????
     p2.type="RestAdmin"
   
     
     p1.firstname=request.POST.get('firstname')
     p1.lastname=request.POST.get('lastname')
     p1.Restaurantname=request.POST.get('Restaurantname')
     p1.location=request.POST.get('location')
     p1.typeofshop=request.POST.get('typeofshop')
     p1.email=request.POST.get('email')
     p1.phone=request.POST.get('phone')
     p1.no_ofstaff=request.POST.get('no_ofstaff')
     p1.auth_person=request.POST.get('auth_person')
     p1.p_email=request.POST.get('p_email')
     p1.p_contact=request.POST.get('p_contact')
     p1.username=request.POST.get('username')
     p1.password=request.POST.get('password')
     p1.type="RestAdmin"
     p1.save()
     p.save()
     p2.save()
     return redirect('/a_home/')


def feed(request):
     a1=request.session['username']
     p1=tbl_UserAccount.objects.get(username=a1)
     return render(request,"addfeedback.html",{'data':p1})
def fill1(request):
     p1=tbl_feedback()
     p1.f_id=request.POST.get('f_id')
     p1.customer_id=request.POST.get('customer_id')
     p1.feedback=request.POST.get('feedback')
     p1.status=request.POST.get('status')
     p1.save()
     return redirect('/u_home/')

def menu1(request):
    a1=request.session['username']
    p1=tbl_RestaurantAccount.objects.get(username=a1)
    return render(request,"addfoodmenu.html",{'data':p1})
def menu2(request):
    p1=tbl_FoodMenu()
    p1.restname=request.POST.get('restname')
    p1.MenuName=request.POST.get('MenuName')
    p1.type=request.POST.get('type')
    p1.cusine=request.POST.get('cusine')
    p1.origin=request.POST.get('origin')
    p1.save()
    return redirect('/r_home/')
def offer(request):
    a1=request.session['username']
    p1=tbl_RestaurantAccount.objects.get(username=a1)
    p2=tbl_FoodMenu.objects.filter(restname=a1)
    return render(request,"addoffers.html",{'data':p1,'data1':p1,"menu":p2})
def offer1(request):
    p1=Offer()
    p1.Res_id=request.POST.get('Res_id')
    p1.MenuItemName=request.POST.get('MenuItemName')
    p1.offer=request.POST.get('offer')
    p1.startdate=request.POST.get('startdate')
    p1.enddate=request.POST.get('enddate')
    p1.details=request.POST.get('details')
    p1.status=request.POST.get('status')
    p1.save()
    return redirect('/r_home/')
def viewoff(request):
    p1=Offer.objects.all()
    return render(request,"viewoffer.html",{'data':p1})
def viewrest(request):
    a1=request.session['username']
    b1=User.objects.get(username=a1)
    p1=tbl_RestaurantAccount.objects.all()
    return render(request,"viewrest.html",{'data1':b1,'data':p1})
def offer2(request):
    a1=request.session['username']
    b1=tbl_UserAccount.objects.get(username=a1)
    p1=Offer.objects.all()
    return render(request,"viewoffer.html",{'data1':b1,'data':p1})
def viewres2(request):
    p1=Offer.objects.all()
    return render(request,"viewrest.html",{'data':p1})
def vfed(request):
    a1=request.session['username']
    b1=tbl_RestaurantAccount.objects.get(username=a1)
    p1=tbl_feedback.objects.all()
    return render(request,"viewfeedback.html",{'data1':b1,'data':p1})
def vwmenu(request):

    p1=tbl_FoodMenu.objects.all()
    return render(request,"viewmenu.html",{'data':p1})
def admin1(request):
     p=User()
     p1=tbl_RestaurantAccount()
     p2=tbl_UserAccount()
     p3=tbl_RestAdmin

     p.username=request.POST.get('username')
     password=request.POST.get('password')
     p.set_password(password)
     p.first_name=request.POST.get('firstname')
     p.last_name=request.POST.get('lastname')
     p.email=request.POST.get('email')
    
     
     p2.firstname=request.POST.get('firstname')
     p2.lastname=request.POST.get('lastname')
     p2.gender="None"
     p2.phone=request.POST.get('phone')
     p2.email=request.POST.get('email')
     p2.address=request.POST.get('location')
     p2.district=request.POST.get('location')
     p2.username=request.POST.get('username')
     p2.state="Kerala"
     p2.type="Restaurant"
   
     
     p1.firstname=request.POST.get('firstname')
     p1.lastname=request.POST.get('lastname')
     p1.Restaurantname=request.POST.get('Restaurantname')
     p1.locatiion=request.POST.get('location')
     p1.typeofshop=request.POST.get('typeofshop')
     p1.email=request.POST.get('email')
     p1.phone=request.POST.get('phone')
     p1.no_ofstaff=request.POST.get('no_ofstaff')
     p1.auth_person=request.POST.get('auth_person')
     p1.p_email=request.POST.get('p_email')
     p1.p_contact=request.POST.get('p_contact')
     p1.username=request.POST.get('username')
     p1.password=request.POST.get('password')
     p1.type="RestAdmin"


     p3.username=request.POST.get('username')
     p3.password=request.POST.get('password')
     p3.restname=request.POST.get('restname')
     p3.email=request.POST.get('email')
     p3.Rest_id=request.POST.get('rest_id')
     p3.type="restaurant"

     p1.save()
     p.save()
     p2.save()
     p3.save()
     return redirect('/')
def update(request,id):
    p1=tbl_RestaurantAccount.objects.get(id=id)
    return render(request,"updatere.html",{'data':p1})
def update1(request,id):
    p1=tbl_RestaurantAccount.objects.get(id=id)
    p1.firstname=request.POST.get('firstname')
    p1.lastname=request.POST.get('lastname')
    p1.Restaurantname=request.POST.get('Restaurantname')
    p1.location=request.POST.get('location')
    p1.typeofshop=request.POST.get('typeofshop')
    p1.email=request.POST.get('email')
    p1.phone=request.POST.get('phone')
    p1.no_ofstaff=request.POST.get('no_ofstaff')
    p1.auth_person=request.POST.get('auth_person')
    p1.p_email=request.POST.get('p_email')
    p1.p_contact=request.POST.get('p_contact')
    p1.save()
    return redirect('/viewrest/')
def item_1(request):
    a1=request.session['username']
    p1=tbl_RestaurantAccount.objects.get(username=a1)
    p2=tbl_FoodMenu.objects.filter(restname=a1)
    return render(request,"addfooditem.html",{'data':p1,"menu":p2})
def item_2(request):
    p1=Fooditem()
    p1.RestaurantName=request.POST.get('RestaurantName')
    p1.MenuName=request.POST.get('MenuName')
    p1.MenuItemName=request.POST.get('MenuItemName')
    p1.Quantity=request.POST.get('Quantity')
    p1.price=request.POST.get('price')
    p1.type=request.POST.get('type')
    p1.cookingtime=request.POST.get('cookingtime')
    p1.status=request.POST.get('status')
    p1.save()
    return redirect('/r_home/')
def updatemenu(request):
    a1= request.session['username']
    b1=tbl_RestaurantAccount.objects.get(username=a1)
    p1=tbl_FoodMenu.objects.filter(restname=a1)
    return render(request,"viewmenu.html",{'data1':b1,'data':p1})
def up_menu11(request,id):
    a1=request.session['username']
    b1=tbl_RestaurantAccount.objects.get(username=a1)
    p1=tbl_FoodMenu.objects.get(id=id)
    return render(request,"updatemenu.html",{'data1':b1,'data':p1})
def up_menu22(request):
    p1=tbl_FoodMenu()
    p1.restname=request.POST.get('restname')
    p1.MenuName=request.POST.get('MenuName')
    p1.type=request.POST.get('type')
    p1.cusine=request.POST.get('cusine')
    p1.origin=request.POST.get('origin')
    p1.save()
    return redirect('/viewmenu/')
def del1(request,id):
    p1=tbl_FoodMenu.objects.get(id=id)
    p1.delete()
    return redirect('/viewmenu/')
def up_item1(request):
    a1= request.session['username']
    b1=tbl_RestaurantAccount.objects.get(username=a1)
    p1=Fooditem.objects.filter(RestaurantName=a1)
    return render(request,"viewitem.html",{'data1':b1,'data':p1})
def up1(request,id):
    a1=request.session['username']
    b1=tbl_RestaurantAccount.objects.get(username=a1)
    p1=Fooditem.objects.get(id=id)
    return render(request,"updateitem.html",{'data1':b1,'data':p1})
def up3(request,id):
    p1=Fooditem.objects.get(id=id)
    p1.RestaurantName=request.POST.get('RestuarantName')
    p1.MenuName=request.POST.get('MenuName')
    p1.MenuItemName=request.POST.get('MenuItemName')
    p1.Quantity=request.POST.get('Quantity') 
    p1.price=request.POST.get('price')
    p1.type=request.POST.get('type')
    p1.cookingtime=request.POST.get('cookingtime')
    p1.status=request.POST.get('status')
    p1.save()
    return redirect('/viewitem/')
def v_fd(request):
    p1=tbl_FoodMenu.objects.all()
    a1=request.session['username']
    b1=tbl_UserAccount.objects.get(username=a1)
    return render(request,"viewfdmenu.html",{'data1':b1,'data':p1})
def v_item1(request):
    a1=request.session['username']
    b1=tbl_UserAccount.objects.get(username=a1)
    p1=Fooditem.objects.all()
    return render(request,"vitem.html",{'data1':b1,'data':p1})
def v_fdbk(request):
    a1=request.session['username']
    b1=tbl_UserAccount.objects.get(username=a1)
    p1=tbl_feedback.objects.all()
    return render(request,"vfeedback.html",{'data1':b1,'data':p1})
def v_res1(request):
    a1=request.session['username']
    b1=tbl_UserAccount.objects.get(username=a1)
    p1=tbl_RestaurantAccount.objects.all()
    return render(request,"vrest.html",{'data1':b1,'data':p1})
def view_fbk(request):
    a1=request.session['username']
    b1=User.objects.get(username=a1)
    p1=tbl_feedback.objects.all()
    return render(request,"v_fdbk.html",{'data1':b1,'data':p1})
def fditm(request):
    p1=Fooditem.objects.all()
    return render(request,"v_fditm.html",{'data':p1})
def fd_mn1(request):
   p1=tbl_FoodMenu.objects.all()
   return render(request,"fd_mn.html",{'data':p1})
def offr2(request):
   p1=Offer.objects.all()
   return render(request,"v_off.html",{'data':p1})
def res2(request):
   p1=tbl_RestaurantAccount.objects.all()
   return render(request,"v_rstn.html",{'data':p1})
def fbk1(request):
    p1=tbl_feedback.objects.all()
    return render(request,"v_fbk1.html",{'data':p1})
def offer3(request):
    a1=request.session['username']
    b1=tbl_RestaurantAccount.objects.get(username=a1)
    p1=Offer.objects.all()
    return render(request,"v_offr1.html",{'data1':b1,'data':p1})
def up_off1(request):
    a1=request.session['username']
    b1=tbl_RestaurantAccount.objects.get(username=a1)
    p1=Offer.objects.all()
    return render(request,"update_offer.html",{'data1':b1,'data':p1})
def updt_off3(request,id):
    p1=Offer.objects.get(id=id)
    p1.Res_id=request.POST.get('Res_id')
    p1.MenuItemName=request.POST.get('MenuItemName')
    p1.offer=request.POST.get('offer')
    p1.startdate=request.POST.get('startdate')
    p1.enddate=request.POST.get('enddate')
    p1.details=request.POST.get('details')
    p1.status=request.POST.get('status')
    p1.save()
    return redirect('/v_offr1/')

def delt_res(request,id):
    p1=tbl_RestaurantAccount.objects.get(id=id)
    data=User.objects.get(username=p1.username)
    data1=tbl_UserAccount.objects.get(username=p1.username)
    p1.delete()
    data.delete()
    data1.delete()
    return redirect('/viewres/')
def v_w(request):
    a1=request.session['username']
    b1=tbl_UserAccount.objects.get(username=a1)
    p1=tbl_RestaurantAccount.objects.all()
    return render(request,"viewrest1.html",{'data1':b1,'data':p1})
def vi_ew(request,id):
    a1=request.session['username']
    p=tbl_UserAccount.objects.get(username=a1)
    b1=tbl_RestaurantAccount.objects.get(id=id)
    print("res anme",b1.Restaurantname	)
    food_items=Fooditem.objects.filter(RestaurantName=b1.username)
    return render(request,"view.html",{'data1':p,'data':food_items,'data3':b1})
def addtocart(request,id):
    f1=Fooditem.objects.get(id=id)
    print(f1.RestaurantName,"Helooooooooooo")
    r1=tbl_RestaurantAccount.objects.get(username=f1.RestaurantName)
    print(r1.Restaurantname,"restname")
    a1=request.session['username']
    p1=tbl_UserAccount.objects.get(username=a1)
    # c1=tbl_FoodMenu.objects.get(restname=r1.Restaurantname)
    return render(request,"cart.html",{'data':p1,"menu":f1})

def add_cart(request):
    p1=tbl_cart()
    p1.restname=request.POST.get('restname')
    p1.fooditemname=request.POST.get('fooditemname')
    p1.quantity=request.POST.get('quantity')
    r1=Fooditem.objects.get(RestaurantName=p1.restname ,MenuItemName=p1.fooditemname)
    p1.price=r1.price
    a=int(p1.quantity)
    b=int(p1.price)
    print(a,"types",b)
    print(type(p1.quantity),"welcome ",type(p1.price))
    p1.totalprice=int(p1.quantity)*int(p1.price)
    p1.status="in cart"
    p1.save()
    return redirect('/u_home/')
def v_cart(request):
    a1=request.session['username']
    b1=tbl_UserAccount.objects.get(username=a1)
    c1=tbl_cart.objects.filter(status="in cart",username=a1)
    return render(request,"viewcart.html",{'data1':b1,'data':c1})
def or_der(request,id):
    a1=request.session['username']
    p=tbl_UserAccount.objects.get(username=a1)
    p1=tbl_cart.objects.get(id=id)
    return render(request,"order.html",{'data1':p,'data':p1})
def order(request,id):
    a1=tbl_order()
    a2=tbl_cart.objects.get(id=id)
    a2.status="in order"
    a2.save()
    a1.username=request.POST.get('username')
    a1.restname=request.POST.get('restname')
    a1.totalprice=request.POST.get('totalprice') 
    a1.paymentmode=request.POST.get('paymentmode')
    a1.status="order processing"
    a1.save()
    return redirect('/u_home/')
def vieworder(request):
    a1=request.session['username']
    p1=tbl_RestaurantAccount.objects.get(username=a1)
    c1=tbl_order.objects.filter(restname=a1)
    return render(request,"vieworder.html",{'data1':p1,'data':c1})
def order1(request):
    a1=request.session['username']
    p1=tbl_UserAccount.objects.get(username=a1)
    c1=tbl_order.objects.filter(username=a1)
    return render(request,"v_order.html",{'data1':p1,'data':c1})
def change0(request,id):
    a1=request.session['username']
    p1=tbl_RestaurantAccount.objects.get(username=a1)
    p=tbl_order.objects.get(id=id)
    return render(request,"change.html",{'data1':p1,'data':p})
def change1(request,id):
    a1=tbl_order.objects.get(id=id)
    a1.username=request.POST.get('username')
    a1.restname=request.POST.get('restname')
    a1.totalprice=request.POST.get('totalprice') 
    a1.paymentmode=request.POST.get('paymentmode')
    a1.status=request.POST.get('status')
    a1.save()
    return redirect('/vieworder/')


    

 



    



    

    

    
       
# Create your views here.
