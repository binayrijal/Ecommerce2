from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import UserLoginForm,MypasswordChangeForm,UserPasswordResetForm,MySetPasswordForm

urlpatterns = [
    path('', views.ProductView.as_view(),name="home"),
    path('product-detail/<int:pk>/', views.product_detail, name='product-detail'),

    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    

    path('cart/',views.show_cart,name="showcart"),
    
    path('plus-cart/',views.plus_cart,name="plus-cart"),

    path('minus-cart/',views.minus_cart,name="minus-cart"),

    path('remove-cart/',views.remove_cart,name="remove-cart"),

    path('buy/', views.buy_now, name='buy-now'),

    path('profile/', views.MyCustomerView.as_view(), name='profile'),

    path('address/', views.address, name='address'),

    path('orders/', views.orders, name='orders'),

    path('changepassword/', auth_views.PasswordChangeView.as_view(template_name='app/changepassword.html',form_class=MypasswordChangeForm,success_url='/passwordchangedone/'), name='changepassword'),
    
    path('passwordchangedone/',auth_views.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'),name='passwordchangedone'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobilelist/<slug:data>',views.mobile,name='mobiledata'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='app/login.html',authentication_form=UserLoginForm),name="loginuser"),
    path('logout/',auth_views.LogoutView.as_view(next_page='loginuser'),name='logout'),
    path('registration/', views.customerregistration, name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='app/password-reset.html',form_class=UserPasswordResetForm),name='password_reset'),
    path('password-reset-done/',auth_views.PasswordResetDoneView.as_view(template_name='app/password-reset-done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='app/password-reset-confirm.html',form_class=MySetPasswordForm),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='app/password-reset-complete.html'),name='password_reset_complete'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
