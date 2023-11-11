from django.shortcuts import render
from django.views import View
from .models import OrderPlaced,Cart,Customer,Product
from .forms import UserRegistrationForm,MyCustomerForm
from django.contrib import messages

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



def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')



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

def checkout(request):
 return render(request, 'app/checkout.html')


class MyCustomerView(View):
 def get(self,request):

  form=MyCustomerForm()
  return render(request,'app/profile.html',{'form':form})
 
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
   messages.success(request,'congratulation!! profile added successfully')
  return render(request,'app/profile.html',{'form':form,'active':' btn-primary'})
   
