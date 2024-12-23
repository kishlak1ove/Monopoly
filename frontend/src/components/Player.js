import React, { useEffect, useState } from 'react';
import axios from 'axios';
import "../styles/style_Player.css";

export default function Player() {
    const [player, setPlayer] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchPlayerData = async () => {
            try {
                const response = await axios.get('http://localhost:8000/api/player');
                setPlayer(response.data);
            } catch (error) {
                console.error("Ошибка при загрузке данных игрока:", error);
            } finally {
                setLoading(false);
            }
        };

        fetchPlayerData();
    }, []);

    if (loading) {
        return <div>Загрузка...</div>;
    }

    if (!player) {
        return <div>Ошибка: Игрок не найден.</div>;
    }

    return (
        <div className='profile_container_main'>
            <div className="content_main_head">
                <h1>Профиль игрока</h1>
            </div>

            <div className="profile_container">
                <div className="player_info">
                    <img className="avatar" src={player.avatar || 'https://via.placeholder.com/150'} alt={`${player.username} Avatar`} />
                    <div className="player_details">
                        <h2>{player.username} <span style={{ color: 'gray' }}>({player.user_id})</span></h2>
                    </div>
                </div>

                <div className="skins_section">
                    <h2>Скины в наличии</h2>
                    <ul className="skin_list">
                        {player.skinsOwned && player.skinsOwned.map((skin, index) => (
                            <li key={index} className="skin_item">{skin}</li>
                        ))}
                    </ul>
                </div>

                <div className="achievements_section">
                    <h2>Достижения</h2>
                    <ul className="achievement_list">
                        {player.achievements && player.achievements.map((ach) => (
                            <li key={ach.id} className="achievement_item">{ach.title}</li>
                        ))}
                    </ul>
                </div>
            </div>
        </div>
    );
}

export { Player }