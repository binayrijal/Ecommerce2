from django.shortcuts import render
from django.views import View
from .models import OrderPlaced,Cart,Customer,Product

#def home(request):
# return render(request, 'app/home.html')

class ProductView(View):
  
  def get(self,request):
   topwears=Product.objects.filter(category='TW')
   bottomwears=Product.objects.filter(category='BW')
   mobiles=Product.objects.filter(category='M')

   # do here laptop 

   return render(request,'app/home.html',{

    'topwears':topwears,

    'bottomwears': bottomwears,

    'mobiles': mobiles,
    
    })

def product_detail(request,pk):
 product_one=Product.objects.get(pk=pk)
 price=product_one.selling_price-product_one.discounted_price
 if product_one:
  return render(request, 'app/productdetail.html',{
   'product_one' :product_one,
   'price' :price
  })

def add_to_cart(request):

  return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request,data=None):
 mobile_sets=None
 if data == None:
  mobile_sets=Product.objects.filter(category='M')
 elif data=="redmi" or data=="iphone" or data=="motorola":
  mobile_sets=Product.objects.filter(category='M').filter(brand=data)
 
 return render(request, 'app/mobile.html',{'mobile_sets':mobile_sets})

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
