import "../styles/style_Game.css";

import React, { useState, useEffect } from 'react';

import c1 from "../employ/c1.png";
import c2 from "../employ/c2.png"; // Альтернативные изображения для фишек
import c3 from "../employ/c3.png";
import c4 from "../employ/c4.png";
import c5 from "../employ/c5.png";
import c6 from "../employ/c6.png";
import board from "../employ/board.png";

export default function Game() {
    const [settings] = useState({
        roomName: "Monopoly Room",
        players: ["Игрок 1", "Игрок 2", "Игрок 3"], // Пример игроков
        maxPlayers: 4,
        startingAmount: 1500,
        gameTime: 60, // Время игры в минутах
        isPrivate: false,
    });

    const [timer, setTimer] = useState(60); // Устанавливаем таймер в 60 минут
    const [diceRoll, setDiceRoll] = useState([1, 1]);
    const [showDice, setShowDice] = useState(false);

    // Таймер уменьшения времени
    useEffect(() => {
        const countdown = setInterval(() => {
            setTimer(prev => prev > 0 ? prev - 1 : 0);
        }, 60000); // Каждую минуту

        return () => clearInterval(countdown);
    }, []);

    // Бросок кубиков
    const rollDice = () => {
        const die1 = Math.floor(Math.random() * 6) + 1;
        const die2 = Math.floor(Math.random() * 6) + 1;
        setDiceRoll([die1, die2]);
        setShowDice(true);
    };

    useEffect(() => {
        if (showDice) {
            const timeout = setTimeout(() => setShowDice(false), 1000); // Показ 1 секунду
            return () => clearTimeout(timeout);
        }
    }, [showDice]);

    return (
        <div className="game-container">
            <header className="game-header">
                <h1>{settings.roomName}</h1>
                <div className="game-info">
                    <p>Осталось времени: {timer} минут</p>
                    <p>Игроки: {settings.players.join(', ')}</p>
                    <button onClick={rollDice} class="header_button_">Бросить кубики</button>
                </div>
            </header>

            {showDice && (
                <div className="dice-result">
                    <h2>Результат броска:</h2>
                    <div className="dice">
                        <span>{diceRoll[0]}</span>
                        <span>{diceRoll[1]}</span>
                    </div>
                </div>
            )}

            <div className="game-board">
                <img src={board} alt="Игровая доска" className="board-image" />
                
                <div className="player-positions">
                    {settings.players.map((player, index) => (
                        <div key={index} className="player-position">
                            <img src={index % 6 === 0 ? c1 : index % 6 === 1 ? c2 : index % 6 === 2 ? c3 : index % 6 === 3 ? c4 : index % 6 === 4 ? c5 : c6} 
                                 alt={player} 
                                 className="player-token" />
                            <p>{player}</p>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
}

export { Game };