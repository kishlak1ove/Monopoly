import React, { useState } from 'react';
import Slider from '../slider/Slider'
import "../styles/style_Shop.css"
import cube_1 from "../employ/cube_1.png"
import cube_2 from "../employ/cube_2.png"
import board_1 from "../employ/board_1.png"
import board_2 from "../employ/board_2.png"
import money from "../employ/money.png"

export default function Shop() {

  const skinsForBoard = [
    {
        id: 1,
        name: 'Скин для доски 1',
        description: 'Описание скина для доски 1.',
        price: 125,
        image: cube_1,
    },
    {
        id: 2,
        name: 'Скин для доски 2',
        description: 'Описание скина для доски 2.',
        price: 200,
        image: cube_2,
    }
  ];

  const skinsForDice = [
    {
        id: 1,
        name: 'Скин для кубика 1',
        description: 'Описание скина для кубика 1.',
        price: 150,
        image: board_1,
    },
    {
        id: 2,
        name: 'Скин для кубика 2',
        description: 'Описание скина для кубика 2.',
        price: 180,
        image: board_2,
    }
  ];
    const [currentAmount, setCurrentAmount] = useState(300);

    const handlePurchase = (price) => {
        if (currentAmount >= price) {
            setCurrentAmount(currentAmount - price);
            alert(`Вы купили скин за ${price} монет!`);
        } else {
            alert('У вас недостаточно монет для этой покупки!');
        }
    };

  return (
  <div className="shop_main_container">
    <div className="shop_container">
    <div className="content_main_head">
      <h1>Магазин монополии</h1>
      <h2>Покупайте скины для игровой доски и кубика, чтобы сделать игру более красочной.</h2>
    </div>
    <Slider />
    <br></br>

    <div className="skins_section">
      <div className='amount_shop_player'>
        <p className="current_amount">Текущая сумма: <strong>{currentAmount}</strong></p>
        <img src={money} height="50" width="50" alt="Money Icon" />
      </div>
        <h2>Скины для доски:</h2>
        <div className="skin-grid">
            {skinsForBoard.map((skin) => (
                <div className="skin-card" key={skin.id}>
                    <img className="skin-image" src={skin.image} alt={skin.name} />
                    <h3>{skin.name}</h3>
                    <p>{skin.description}</p>
                    <button className="button_game_create" onClick={() => handlePurchase(skin.price)}>
                        Купить за {skin.price} монет
                    </button>
                </div>
            ))}
        </div>

        <h2>Скины для кубика:</h2>
        <div className="skin-grid">
            {skinsForDice.map((skin) => (
                <div className="skin-card" key={skin.id}>
                    <img className="skin-image" src={skin.image} alt={skin.name} />
                    <h3>{skin.name}</h3>
                    <p>{skin.description}</p>
                    <button className="button_game_create" onClick={() => handlePurchase(skin.price)}>
                        Купить за {skin.price} монет
                    </button>
                </div>
            ))}
        </div>
      </div>
    </div>
  </div>
  )
}
export { Shop }
