from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer, OptionSerializer, OptionlistSerializer,CartSerializer, CartItemSerializer, OrderSerializer
from .models import Product, OptionList, Option, Cart, CartItem, Order

# Create your views here.

class ProductsView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializers = ProductSerializer(products, many=True)
        return Response(serializers.data, status=200)


class ProductView(APIView):
    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        serializers = ProductSerializer(product)
        return Response(serializers.data, status=200)

class AddToCart(APIView):
    def post(self, request):
        product = Product.objects.get(id=request.data['product'])
        cart = Cart.objects.get(id=request.data['cart'])
        addOns = request.data['addOns']
        cartItem = CartItem.objects.create(product=product, quantity=request.data['quantity'], totalPrice=request.data['totalPrice'])
        for addOn in addOns:
            option = Option.objects.get(id=addOn)
            cartItem.addOns.add(option)
        cart.cartItems.add(cartItem)
        cart.totalQuantity += 1
        cart.grandTotal += request.data['totalPrice']
        cart.save()
        return Response("Item added", status=200)

    def get(self,request,pk):
        cart = Cart.objects.get(id=1)
        cartItem = cart.cartItems.get(product=pk)
        cart.grandTotal += cartItem.totalPrice/cartItem.quantity
        cartItem.totalPrice += cartItem.totalPrice/cartItem.quantity
        cartItem.quantity += 1
        cart.totalQuantity += 1
        cartItem.save()
        cart.save()
        return Response('Item quantity increased', status=200)

class DeleteFromCart(APIView):
    def get(self, request, pk):
        cart = Cart.objects.get(id=1)
        cartItem = cart.cartItems.get(product=pk)
        cart.grandTotal -= cartItem.totalPrice/cartItem.quantity
        cart.totalQuantity -= 1
        if(cartItem.quantity > 1):
            cartItem.totalPrice -= cartItem.totalPrice/cartItem.quantity
            cartItem.quantity -= 1
            cartItem.save()
            cart.save()
            return Response('Item quantity decreased', status=200)
        cartItem.delete()
        cart.save()
        return Response('Item deleted from cart', status=200)

class DeleteCartItem(APIView):
    def get(self, request, pk):
        cart = Cart.objects.get(id=1)
        cartItem = cart.cartItems.get(product=pk)
        cart.grandTotal -= cartItem.totalPrice
        cart.totalQuantity -= cartItem.quantity
        cartItem.delete()
        cart.save()
        return Response('Item deleted from cart', status=200)
    

class ClearCart(APIView):
    def get(self, request,pk):
        cart = Cart.objects.get(id=pk)
        cart.cartItems.clear()
        cart.grandTotal = 0
        cart.totalQuantity = 0
        cart.save()
        return Response('Cart cleared', status=200)

class CreateCart(APIView):
    def post(self, request):
        cart = Cart.objects.create(grandTotal=0, totalQuantity=0)
        return Response('Cart created', status=200)

        
class CartView(APIView):
    def get(self, request,pk):
        cart = Cart.objects.get(id=pk)
        serializers = CartSerializer(cart)
        return Response(serializers.data, status=200)


