import React, { useState } from 'react';
import "../styles/style_Create.css"
import axios from 'axios';
import { useNavigate  } from 'react-router-dom';

export default function Create() {

  const [roomName, setRoomName] = useState('');
  const [maxPlayers, setMaxPlayers] = useState(2);
  const [startingAmount, setStartingAmount] = useState(1500);
  const [gameTime, setGameTime] = useState(60);
  const [isPrivate, setIsPrivate] = useState(false);
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
        e.preventDefault();
        setError(''); 

        if (!roomName) {
        setError('Название комнаты обязательно.');
        return;
        }
        if (startingAmount <= 0) {
            setError('Начальная сумма должна быть положительным числом.');
            return;
        }
        if (gameTime <= 0) {
            setError('Время игры должно быть положительным числом.');
            return;
        }

        try {
            const response = await axios.post('http://localhost:8000/api/rooms/', {
                room_name: roomName,
                max_players: maxPlayers,
                starting_amount: startingAmount,
                game_time: gameTime,
                is_private: isPrivate,
            });

            if (response && response.data && response.data.id) {
                navigate(`/room/${response.data.id}`, {
                    state: {
                        roomName: roomName,
                        maxPlayers: maxPlayers,
                        startingAmount: startingAmount,
                        gameTime: gameTime,
                        isPrivate: isPrivate,
                    },
                });
            } else {
                setError('Полученные данные не содержат ID нового объекта комнаты.');
            }
        } catch (error) {
            if (error.response) {
                setError('Ошибка при создании комнаты: ' + (error.response.data.detail || error.message));
            } else if (error.request) {
                setError('Сервер не ответил. Попробуйте позже.');
            } else {
                setError('Ошибка: ' + error.message);
            }
        }
    };
  return (
  <div className="room-setup">
    <div className="content_main_head">
        <h1>Настройка комнаты для Монополии</h1>
        <h2>Заполните информацию, чтобы начать игру.</h2>
    </div>

    <form onSubmit={handleSubmit} className="setup_form">
        <div className="form_group">
            <label>Название комнаты:</label>
            <input 
                type="text" 
                value={roomName} 
                onChange={(e) => setRoomName(e.target.value)} 
                required 
            />
        </div>
        <div className="form_group">
            <label>Количество игроков:</label>
            <select 
                value={maxPlayers} 
                onChange={(e) => setMaxPlayers(Number(e.target.value))} 
            >
                <option value={2}>2</option>
                <option value={3}>3</option>
                <option value={4}>4</option>    
            </select>
        </div>
        <div className="form_group">
            <label>Начальная сумма:</label>
            <input 
                type="number" 
                value={startingAmount} 
                onChange={(e) => setStartingAmount(Number(e.target.value))} 
                min="0" 
                required 
            />
        </div>
        <div className="form_group">
            <label>Время игры (в минутах):</label>
            <input 
                type="number" 
                value={gameTime} 
                onChange={(e) => setGameTime(Number(e.target.value))} 
                min="1" 
                required 
            />
        </div>
        <div className="form_group">
            <label>
                <input
                    type="checkbox"
                    checked={isPrivate}
                    onChange={(e) => setIsPrivate(e.target.checked)}
                />
                Приватная комната
            </label>
        </div>

        <button type="submit" className="button_game_create">Создать комнату</button>
        {error && <p style={{ color: 'red' }}>{error}</p>}
    </form>
  </div>
  )
}

export { Create }