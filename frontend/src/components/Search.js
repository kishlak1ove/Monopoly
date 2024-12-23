import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import "../styles/style_Search.css"

export default function Search() {
    const [rooms, setRooms] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState('');

    useEffect(() => {
        const fetchRooms = async () => {
            try {
                const response = await axios.get('http://localhost:8000/api/room/');
                setRooms(response.data);
            } catch (error) {
                setError('Ошибка при загрузке комнат: ' + error.message);
            } finally {
                setLoading(false);
            }
        };

        fetchRooms();
    }, []);

    if (loading) return <div>Загрузка...</div>;
    if (error) return <div style={{ color: 'red' }}>{error}</div>;
  return (
    
    <div className="game-search-container">
        <h1>Поиск игр</h1>
        <h2>Доступные комнаты</h2>
        <ul className="room-list">
            {rooms.length === 0 ? (
                <li>Нет доступных комнат</li>
            ) : (
                rooms.map((room) => (
                    <li key={room.id} className="room-item">
                        <div>
                            <h3>{room.name}</h3>
                            <p>{room.isGameRunning ? 'Игра идет' : 'Ожидание игроков'}</p>
                            <p>Максимальное количество игроков: {room.maxPlayers}</p>
                            {room.isGameRunning && (
                                <p>Оставшееся время: {room.remainingTime} минут</p> // Вам нужно будет добавить логику сохранения remainingTime на сервере
                            )}
                            <Link to={`/room/${room.id}`} className="join-button">
                                Присоединиться
                            </Link>
                        </div>
                    </li>
                ))
            )}
        </ul>
    </div>
  )
}

export { Search }