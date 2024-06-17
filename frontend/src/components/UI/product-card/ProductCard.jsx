import React from "react";
import "../../../styles/product-card.css";
import { Link } from "react-router-dom";
import { useDispatch } from "react-redux";
import { cartActions } from "../../../store/shopping-cart/cartSlice";
import { useState } from "react";
import { set } from "mongoose";

const ProductCard = (props) => {
  const { id, name, image01, price, optionslists } = props.item;
  const dispatch = useDispatch();

  const [price1, setPrice1] = useState(30);
  const [price2,setPrice2] = useState(0);
  const [price3,setPrice3] = useState(0);

  const totalPrice = price + price1 + price2 + price3;

  const addToCart = () => {
    const resp = dispatch(
      cartActions.addItem({
        id,
        name,
        totalPrice,
      })
    );
  };


  return (
    <div className="product__item">
      <div className="product__img">
        <img src={image01} alt="product-img" className="w-50" />
      </div>

      <div className="product__content">
        <h5>
          <Link to={`/foods/${id}`}>{name}</Link>
        </h5>
          <div className="product__addOns">
            <h6>{optionslists[0].name}*</h6>
            <select name="options-list"
             onChange={e => setPrice1(optionslists[0].options[e.target.value - 2].price) }>
              {optionslists[0].options.map((option) => (
                <option key={option.id} value={option.id}>
                  {option.name}
                  {option.price && `  ₹${option.price}`}
                </option>
              ))}
            </select>
         </div>
          <div className="product__addOns">
            <h6>{optionslists[1].name}</h6>
            <select name="options-list" 
            onChange={ e => {
              if(e.target.value !=='1'){
                setPrice2(optionslists[1].options[e.target.value - 8].price)
              }
              else
                setPrice2(0);
            } }>
              {optionslists[1].options.map((option) => (
                <option key={option.id} value={option.id}>
                  {option.name}
                  {option.price && `  ₹${option.price}`}
                </option>
              ))}
            </select>
         </div>
          <div className="product__addOns">
            <h6>{optionslists[2].name}</h6>
            <select name="options-list" onChange={(e) =>{
              
              if(e.target.value !=='1'){
                setPrice3(optionslists[2].options[e.target.value - 12].price)
              }
              else
                setPrice3(0);
            } }>

              {optionslists[2].options.map((option) => (
                <option key={option.id} value={option.id}>
                  {option.name}
                  {option.price && `  ₹${option.price}`}
                </option>
              ))}
            </select>
         </div>

        <div className=" d-flex align-items-center justify-content-between ">
          <span className="product__price">₹{totalPrice}</span>
          <button className="addTOCart__btn" onClick={addToCart}>
            Add to Cart
          </button>
        </div>
      </div>
    </div>
  );
};

export default ProductCard;
