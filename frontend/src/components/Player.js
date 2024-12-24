import React from 'react';
import axios from 'axios';

const Player = ({ player, updatePlayerData }) => {
    const handleMove = async () => {
        try {
            const response = await axios.patch(`http://localhost:8000/api/player/${player.id}/move/`);
            updatePlayerData(response.data); // Обновляем данные игрока
        } catch (error) {
            console.error('Ошибка при передвижении игрока:', error);
        }
    };

    const handleBuy = async (realtyId) => {
        try {
            const response = await axios.patch(`http://localhost:8000/api/player/${player.id}/buy/`, { realty: realtyId });
            alert(response.data.message);
        } catch (error) {
            console.error('Ошибка при покупке:', error);
        }
    };

    return (
        <div>
            <h2>Игрок: {player.username}</h2>
            <button onClick={handleMove}>Двигаться</button>
            {/* Вызов функции handleBuy с ID недвижимости может быть добавлен или удален в зависимости от вашей логики */}
        </div>
    );
};

export default Player;