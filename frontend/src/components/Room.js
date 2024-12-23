import React, { useEffect, useState } from 'react';
import { useLocation, useParams } from 'react-router-dom';
import "../styles/style_Room.css"

export default function Room() {

  const players = [
    { name: 'Игрок 1', avatar: 'https://via.placeholder.com/150' },
    { name: 'Игрок 2', avatar: 'https://via.placeholder.com/150' },
    { name: 'Игрок 3', avatar: 'https://via.placeholder.com/150' },
    { name: 'Игрок 4', avatar: 'https://via.placeholder.com/150' },
  ];

    const { roomId } = useParams();
    const location = useLocation();
    const { state } = location;

    const roomSettings = {
        roomName: state?.name || 'Неизвестная комната',
        maxPlayers: state?.player_count || 0,
        startingAmount: state?.init_score || 0,
        gameTime: state?.gameTime || 0,
        isPrivate: state?.is_private || false,
    };

    const handleStartGame = () => {
        setIsCounting(true); 
    };

    const [countdown, setCountdown] = useState(5);
    const [isCounting, setIsCounting] = useState(false);

    useEffect(() => {
        let timer;
        if (isCounting && countdown > 0) {
            timer = setInterval(() => {
                setCountdown((prev) => prev - 1);
            }, 1000);
        } else if (countdown === 0) {
            console.log('Игра началась!');
            setIsCounting(false);
            setCountdown(5);
        }
        return () => clearInterval(timer);
    }, [isCounting, countdown]);

  return (
    <div className="room-container">
        <div className="room-header">
            <h1>{roomSettings.roomName}</h1>
            <br></br>
            <h2>Настройки игры</h2>
        </div>

        <div className="room-settings">
            <ul>
                <li>Максимальное количество игроков: {roomSettings.maxPlayers}</li>
                <li>Начальная сумма: {roomSettings.startingAmount}</li>
                <li>Время игры (мин): {roomSettings.gameTime}</li>
                <li>Приватная комната: {roomSettings.isPrivate ? 'Да' : 'Нет'}</li>
            </ul>
        </div>

        <h2>Игроки</h2>
        <div className="players-container">
            {players.map((player, index) => (
                <div key={index} className="player-card">
                    <img src={player.avatar} alt={player.name} className="player-avatar" />
                    <p>{player.name}</p>
                </div>
            ))}
        </div>

        {isCounting ? (
                <div>
                    <h2>Обратный отсчет: {countdown}</h2>
                </div>
            ) : (
                <button className="button_start_game" onClick={handleStartGame}>Начать игру</button>
            )}
    </div>
  )
}

export { Room }