from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import UserLoginForm,MypasswordChangeForm

urlpatterns = [
    path('', views.ProductView.as_view(),name="home"),

    path('product-detail/<int:pk>/', views.product_detail, name='product-detail'),

    path('cart', views.add_to_cart, name='add-to-cart'),

    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', auth_views.PasswordChangeView.as_view(template_name='app/changepassword.html',form_class=MypasswordChangeForm), name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobilelist/<slug:data>',views.mobile,name='mobiledata'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='app/login.html',authentication_form=UserLoginForm),name="loginuser"),
    path('logout/',auth_views.LogoutView.as_view(next_page='loginuser'),name='logout'),
    path('registration/', views.customerregistration, name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
