from django.shortcuts import render,redirect
from django.views import View
from .models import OrderPlaced,Cart,Customer,Product
from .forms import UserRegistrationForm,MyCustomerForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



#def home(request):
# return render(request, 'app/home.html')


class ProductView(View):
  
  def get(self,request):
   total=0
   topwears=Product.objects.filter(category='TW')
   bottomwears=Product.objects.filter(category='BW')
   mobiles=Product.objects.filter(category='M')
   if request.user.is_authenticated:
     total=len(Cart.objects.filter(user=request.user))

   # do here laptop 

   return render(request,'app/home.html',{

    'topwears':topwears,

    'bottomwears': bottomwears,

    'mobiles': mobiles,
    'total':total,
    
    })


def product_detail(request,pk):
 product_one=Product.objects.get(pk=pk)
 price=product_one.selling_price-product_one.discounted_price
 item_already_exist=False
 if request.user.is_authenticated:
  item_already_exist=Cart.objects.filter(Q(product=product_one.id) & Q(user=request.user)).exists()
 if product_one:
  return render(request, 'app/productdetail.html',{
   'product_one' :product_one,
   'price' :price,
   'item_already_exist':item_already_exist,
  })

@login_required
def add_to_cart(request):
  
  user=request.user
  pro_id=request.GET.get('prod_id')
  product=Product.objects.get(id=pro_id)
  Cart(user=user,product=product).save()
  
  return redirect('/cart')



def show_cart(request):
 total=0
 if request.user.is_authenticated:
  
  user=request.user
  cart=Cart.objects.filter(user=user)
  amount=0.0
  shipping=70.0
  total_amount=0.0
  product_cart=[p for p in Cart.objects.all() if p.user==request.user]
  total=len(Cart.objects.filter(user=request.user))

  if product_cart:
   for p in product_cart:
    price=p.product.selling_price-p.product.discounted_price
    tempamount=(p.quantity*price)
    amount=amount+tempamount
   total_amount=amount+shipping
  return render(request,'app/addtocart.html',{'carts':cart,'amount':amount,'total_amount':total_amount,'total':total})


def plus_cart(request):
 if request.method=="GET":
  prod_id=request.GET['prod_id']
  pluscart=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
  pluscart.quantity+=1
  pluscart.save()
  amount=0.0
  shipping=70.0

  product_cart=[p for p in Cart.objects.all() if p.user==request.user]

  for p in product_cart:
   price=p.product.selling_price-p.product.discounted_price
   
   tempamount=(p.quantity*price)
   amount+=tempamount
  totalamount=amount+shipping

  data={
   'quantity':pluscart.quantity,
   'amount':amount,
   'totalamount':totalamount,
  }
  return JsonResponse(data)
 

def minus_cart(request):
 if request.method=="GET":
  prod_id=request.GET['prod_id']
  pluscart=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
  pluscart.quantity-=1
  pluscart.save()
  amount=0.0
  shipping=70.0

  product_cart=[p for p in Cart.objects.all() if p.user==request.user]

  for p in product_cart:
   
   tempamount=(p.quantity*p.product.selling_price)
   amount+=tempamount
  totalamount=amount+shipping

  data={
   'quantity':pluscart.quantity,
   'amount':amount,
   'totalamount':totalamount,
  }
  return JsonResponse(data)

def remove_cart(request):
 if request.method=="GET":
  prod_id=request.GET['prod_id']
  pluscart=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
  
  pluscart.delete()
  amount=0.0
  shipping=70.0

  product_cart=[p for p in Cart.objects.all() if p.user==request.user]

  for p in product_cart:
   
   tempamount=(p.quantity*p.product.selling_price)
   amount+=tempamount
  totalamount=amount+shipping

  data={
   'quantity':pluscart.quantity,
   'amount':amount,
   'totalamount':totalamount,
  }
  return JsonResponse(data)












def buy_now(request):
 return render(request, 'app/buynow.html')


@login_required
def address(request):
 user=request.user
 obj=Customer.objects.filter(user=user)

 return render(request, 'app/address.html',{'obj':obj,'active':'btn-primary'})

def orders(request):
 order=OrderPlaced.objects.filter(user=request.user)
 
 return render(request, 'app/orders.html',{
  'order':order,
 })



def mobile(request,data=None):
 mobile_sets=None
 if data == None:
  mobile_sets=Product.objects.filter(category='M')
 elif data in ["redmi","iphone","Motorola"]:
  mobile_sets=Product.objects.filter(category='M').filter(brand=data)
 elif data=='below':
  mobile_sets=Product.objects.filter(category='M').filter(selling_price__lt=30000.0)
 elif data=='above':
  mobile_sets=Product.objects.filter(category='M').filter(selling_price__gte=30000.0)
 
 return render(request, 'app/mobile.html',{'mobile_sets':mobile_sets})


def login(request):
 return render(request, 'app/login.html')


def customerregistration(request):
 if request.method=="POST":
  form=UserRegistrationForm(request.POST)
  if form.is_valid():
     form.save()
     messages.success(request,'congratulations!!Registration successfull')
     form=UserRegistrationForm()
     
 else:
  form=UserRegistrationForm()

 return render(request, 'app/customerregistration.html',{
  'form':form,
 })


@login_required
def checkout(request):
 add=Customer.objects.filter(user=request.user)
 cart_item=Cart.objects.filter(user=request.user)
 amount=0.0
 shipping=70.0
 cart_product=[p for p in Cart.objects.all() if p.user==request.user]
 for p in cart_product:
  tempamount=(p.quantity*p.product.lastprice)
  amount+=tempamount
 totalamount=amount+shipping
 return render(request, 'app/checkout.html',{'add':add,'totalamount':totalamount,'cartitem':cart_item})

@login_required
def payment_done(request):
 cust_id=request.GET.get('custid')
 cust=Customer.objects.get(id=cust_id)
 cart=Cart.objects.filter(user=request.user)
 for c in cart:
   OrderPlaced(user=request.user,customer=cust,product=c.product,quantity=c.quantity).save()
   c.delete()
 return redirect("orders")
 





@method_decorator(login_required,name='dispatch')
class MyCustomerView(View):
 def get(self,request):

  form=MyCustomerForm()
  return render(request,'app/profile.html',{'form':form,'active':'btn-primary'})
 
 def post(self,request):
  form=MyCustomerForm(request.POST)
  if form.is_valid():
   user=request.user
   name=form.cleaned_data['name']
   locality=form.cleaned_data['locality']
   city=form.cleaned_data['city']
   state=form.cleaned_data['state']
   zipcode=form.cleaned_data['zipcode']
   reg=Customer( user=user, name=name, locality=locality, city=city, state=state, zipcode=zipcode)
   reg.save()
   form=MyCustomerForm()
   messages.success(request,'congratulation!! profile added successfully look it into address section')
  return render(request,'app/profile.html',{'form':form,'active':' btn-primary'})
   
