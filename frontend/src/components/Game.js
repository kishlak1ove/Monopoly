import React from 'react';
import "../styles/style_Game.css";
import c1 from "../employ/c1.png"
import c2 from "../employ/c1.png"
import c3 from "../employ/c1.png"
import c4 from "../employ/c1.png"
import c5 from "../employ/c1.png"
import c6 from "../employ/c1.png"
import board from "../employ/board.png"


export default function Game() {
    // Примерные данные для игроков
    const players = [
        { name: "Игрок 1", money: 1500, position: 0 },
        { name: "Игрок 2", money: 1500, position: 0 },
        { name: "Игрок 3", money: 1500, position: 0 },
        { name: "Игрок 4", money: 1500, position: 0 },
    ];

    return (
        <div className="game-container">
            <div className="game-info">
                <h1>Монополия</h1>
                {/* Предполагаем, что игроки уже инициализированы */}
                <h2>Игрок: {players[0].name} (Деньги: ${players[0].money})</h2>
                <h3>Осталось времени: 30 минут</h3>
                <button onClick={() => alert("Бросок кубика!")}>
                    Бросить кубик
                </button>
                <div className="dice-roll">Вы бросили: 0</div>
            </div>

            <div className="game-board">
                <div className="board">
                    {/* Отображение "недвижимости" как пустые клетки */}
                    {Array.from({ length: 40 }).map((_, index) => (
                        <div className="property" key={index}>
                            <span>Участок {index + 1}</span>
                        </div>
                    ))}
                </div>

                <div className="players-container">
                    {players.map((player, index) => (
                        <div
                            key={index}
                            className={`player-icon`}
                            style={{ left: `${player.position * 10}%` }}
                        >
                            {player.name}
                        </div>
                    ))}
                </div>
            </div>

            <div className="game-over" style={{ display: 'none' }}>Игра закончена!</div>
        </div>
    );
}

export { Game }