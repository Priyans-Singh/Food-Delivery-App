from rest_framework import serializers
from .models import Product, OptionList, Option, Cart, CartItem, Order

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'

class OptionlistSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)
    class Meta:
        model = OptionList
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    optionslists = OptionlistSerializer(many=True)
    class Meta:
        model = Product
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    addOns = OptionSerializer(many=True)
    # product = ProductSerializer()
    class Meta:
        model = CartItem
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    cartItems = CartItemSerializer(many=True)
    class Meta:
        model = Cart
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)
    class Meta:
        model = Order
        fields = '__all__'





