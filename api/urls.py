from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductsView.as_view()),
    path('product/<int:pk>/', views.ProductView.as_view()),
    path('createcart/', views.CreateCart.as_view()),
    path('addtocart/', views.AddToCart.as_view()),
    path('cart/<int:pk>/', views.CartView.as_view()),
    path('deletefromcart/<int:pk>/', views.DeleteFromCart.as_view()),
    path('clearcart/<int:pk>/', views.ClearCart.as_view()),
    path('updatecart/<int:pk>/', views.AddToCart.as_view()),   
    path('deletecartitem/<int:pk>/', views.DeleteCartItem.as_view()),
]