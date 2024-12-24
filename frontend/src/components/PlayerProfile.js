import React from 'react';
import { useAuth } from './AuthContext'; 
import "../styles/style_Player.css";
import userIcon from "../employ/online.png"

export default function PlayerProfile() {
    const { auth } = useAuth(); 

    if (!auth.isLoggedIn) {
        return <div style={{ color: "red" }}>Ошибка: Пользователь не авторизован.</div>;
    }

    return (
        <div className='profile_container_main'>
            <div className="content_main_head">
                <h1>Профиль игрока</h1>
            </div>

            <div className="profile_container">
                <div className="player_info">
                    <img alt="User Icon" className="user_icon"  src={userIcon} />
                    <h2>
                        {auth.user.username} <span style={{ color: 'gray' }}>({auth.user.id})</span> 
                    </h2>
                </div>

                <div className="skins_section">
                    <h2>Скины в наличии</h2>
                    <ul className="skin_list">
                        <li className="skin_item">Нет скинов в наличии</li>
                    </ul>
                </div>

                <div className="achievements_section">
                    <h2>Достижения</h2>
                    <ul className="achievement_list">
                        <li className="achievement_item">Нет достижений</li>
                    </ul>
                </div>
            </div>
        </div>
    );
}

export { PlayerProfile };