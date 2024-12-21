import React, { useEffect, useState } from 'react';
import { useLocation, useParams, useNavigate } from 'react-router-dom';

export default function Game() {

    const BOARD_IMAGE = 'path/to/monopoly_board.jpg'; 

    const playersInitialData = [
        { id: 1, name: 'Игрок 1', avatar: 'https://via.placeholder.com/150', position: 0 },
        { id: 2, name: 'Игрок 2', avatar: 'https://via.placeholder.com/150', position: 0 },
        { id: 3, name: 'Игрок 3', avatar: 'https://via.placeholder.com/150', position: 0 },
        { id: 4, name: 'Игрок 4', avatar: 'https://via.placeholder.com/150', position: 0 },
    ];

    const { roomId } = useParams();
    const location = useLocation();
    const navigate = useNavigate();
    const { state } = location;

    const [players, setPlayers] = useState(playersInitialData);
    const [currentPlayerIndex, setCurrentPlayerIndex] = useState(0);
    const [dieValue, setDieValue] = useState(null);
    const [isGameRunning, setIsGameRunning] = useState(false);
    const [timer, setTimer] = useState(0);

    const roomSettings = {
        roomName: state.roomName || 'Неизвестная комната',
        maxPlayers: state.maxPlayers || 0,
        startingAmount: state.startingAmount || 0,
        gameTime: state.gameTime || 0,
        isPrivate: state.isPrivate || false,
    };

    const rollDice = () => {
        const rolledValue = Math.floor(Math.random() * 6) + 1;
        setDieValue(rolledValue);
        movePlayer(rolledValue);
    };

    const movePlayer = (steps) => {
        setPlayers((prevPlayers) => {
            const newPlayers = [...prevPlayers];
            newPlayers[currentPlayerIndex].position += steps;
            if (newPlayers[currentPlayerIndex].position >= 40) {
                newPlayers[currentPlayerIndex].position -= 40;
            }
            return newPlayers;
        });
        setCurrentPlayerIndex((prevIndex) => (prevIndex + 1) % players.length);
    };

    const handleLeaveGame = () => {
        const shouldLeave = window.confirm("Вы хотите покинуть игру?");
        if (shouldLeave) {
            navigate('/');
        }
    };

    const startGame = () => {
        setIsGameRunning(true);
    };

    useEffect(() => {
        if (roomSettings.gameTime) {
            setTimer(roomSettings.gameTime * 60);
        }
    }, [roomSettings.gameTime]);

    useEffect(() => {
        if (isGameRunning && timer > 0) {
            const id = setInterval(() => {
                setTimer((prev) => {
                    if (prev <= 1) {
                        clearInterval(id);
                        alert("Время вышло!");
                        setIsGameRunning(false);
                        return 0;
                    }
                    return prev - 1;
                });
            }, 1000);
            return () => clearInterval(id);
        }
    }, [isGameRunning, timer]);


  return (
    <div>
        <h1>{roomSettings.roomName}</h1>
        <h2>Игроки</h2>
        <div>
            {players.map(player => (
                <div key={player.id}>
                    <img src={player.avatar} alt={player.name} />
                    <p>{player.name}, Позиция: {player.position}</p>
                </div>
            ))}
        </div>
        <button onClick={startGame}>Начать игру</button>
        {isGameRunning && <p>Игра в процессе... Время: {timer} секунд</p>}
        <button onClick={rollDice} disabled={!isGameRunning}>Бросить кубик</button>
        <button onClick={handleLeaveGame}>Покинуть игру</button>
    </div>
  )
}

export { Game }