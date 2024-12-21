import React from 'react'
import "../styles/style_Player.css"

export default function Player() {
    const player = {
        name: 'Игрок 1',
        avatar: 'https://via.placeholder.com/150', 
        currentAmount: 1500,
        skinsOwned: ['Скин для доски 1', 'Скин для кубика 2'],
        achievements: [
            { id: 1, title: 'Победитель первой игры' },
            { id: 2, title: 'Собрал все скины' }
        ]
    };
  return (
    <div className='profile_container_main'>
        <div className="content_main_head">
            <h1>Профиль игрока</h1>
        </div>
        <div className="profile_container">
            <div className="player_info">
                <img className="avatar" src={player.avatar} alt={`${player.name} Avatar`} />
                <div className="player_details">
                    <h2>{player.name}</h2>
                </div>
            </div>

            <div className="skins_section">
                <h2>Скины в наличии</h2>
                <ul className="skin_list">
                    {player.skinsOwned.map((skin, index) => (
                        <li key={index} className="skin_item">{skin}</li>
                    ))}
                </ul>
            </div>

            <div className="achievements_section">
                <h2>Достижения</h2>
                <ul className="achievement_list">
                    {player.achievements.map((ach, index) => (
                        <li key={ach.id} className="achievement_item">{ach.title}</li>
                    ))}
                </ul>
            </div>
        </div>
    </div>
  )
}

export { Player }