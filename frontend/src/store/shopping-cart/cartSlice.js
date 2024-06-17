import { createSlice } from "@reduxjs/toolkit";
import { set } from "mongoose";

const items =
  localStorage.getItem("cartItems") !== null
    ? JSON.parse(localStorage.getItem("cartItems"))
    : [];

// const items = getCart()

const totalAmount =
  localStorage.getItem("totalAmount") !== null
    ? JSON.parse(localStorage.getItem("totalAmount"))
    : 0;

const totalQuantity =
  localStorage.getItem("totalQuantity") !== null
    ? JSON.parse(localStorage.getItem("totalQuantity"))
    : 0;

const setItemFunc = (item, totalAmount, totalQuantity) => {
  localStorage.setItem("cartItems", JSON.stringify(item));
  localStorage.setItem("totalAmount", JSON.stringify(totalAmount));
  localStorage.setItem("totalQuantity", JSON.stringify(totalQuantity));
};



const addToCart = async (product, quantity, totalPrice, addOns) => {
      const response  = await fetch('api/addtocart/',{
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          cart: 1,
          product: product,
          quantity: quantity,
          totalPrice: totalPrice,
          addOns: addOns,
        })
      });
      const data = await response.json();
}

const increaseQuantity = async (id) => {
  const response  = await fetch(`api/updatecart/${id}/`);
  const data = await response.json();
}

const removeFromCart = async (id) => {
      const response  = await fetch(`api/deletefromcart/${id}`);
      const data = await response.json();
}

const deleteFromCart = async (id) => {
  const response = await fetch(`api/deletecartitem/${id}/`)
  const data = await response.json();
}

const initialState = {
  cartItems: items,
  totalQuantity: totalQuantity,
  totalAmount: totalAmount,
};

const cartSlice = createSlice({
  name: "cart",
  initialState,

  reducers: {
      // addCartData(state, action) {
      //     state.cartItems = action.payload.cartItems;
      //     state.totalAmount = action.payload.totalAmount;
      //     state.totalQuantity = action.payload.totalQuantity;
      // },
    // =========== add item ============
      addItem(state, action) {
      const newItem = action.payload;
      const existingItem = state.cartItems.find(
        (item) => item.id === newItem.id
      );
      state.totalQuantity++;

      if (!existingItem) {
        addToCart(newItem.id,1,newItem.totalPrice,[]);  
        state.cartItems.push({
          id: newItem.id,
          name: newItem.name,
          price: newItem.totalPrice,
          quantity: 1,
          totalPrice: newItem.totalPrice,
        });

      } else {
        increaseQuantity(newItem.id);
        existingItem.quantity++;
        existingItem.totalPrice =
          Number(existingItem.totalPrice) + Number(newItem.totalPrice);
      }

      state.totalAmount = state.cartItems.reduce(
        (total, item) => total + Number(item.price) * Number(item.quantity),
        0
      );

      setItemFunc(
        state.cartItems.map((item) => item),
        state.totalAmount,
        state.totalQuantity
      );
    },

    // ========= remove item ========

    removeItem(state, action) {
      const id = action.payload;
      const existingItem = state.cartItems.find((item) => item.id === id);
      state.totalQuantity--;
      removeFromCart(id);
      if (existingItem.quantity === 1) {
        state.cartItems = state.cartItems.filter((item) => item.id !== id);
      } else {
        existingItem.quantity--;
        existingItem.totalPrice =
          Number(existingItem.totalPrice) - Number(existingItem.price);
      }

      state.totalAmount = state.cartItems.reduce(
        (total, item) => total + Number(item.price) * Number(item.quantity),
        0
      );

      setItemFunc(
        state.cartItems.map((item) => item),
        state.totalAmount,
        state.totalQuantity
      );
    },

    //============ delete item ===========

    deleteItem(state, action) {
      const id = action.payload;
      const existingItem = state.cartItems.find((item) => item.id === id);
      deleteFromCart(id);
      if (existingItem) {
        state.cartItems = state.cartItems.filter((item) => item.id !== id);
        state.totalQuantity = state.totalQuantity - existingItem.quantity;
      }

      state.totalAmount = state.cartItems.reduce(
        (total, item) => total + Number(item.price) * Number(item.quantity),
        0
      );
      setItemFunc(
        state.cartItems.map((item) => item),
        state.totalAmount,
        state.totalQuantity
      );
    },
  },
});

export const cartActions = cartSlice.actions;
export default cartSlice;
