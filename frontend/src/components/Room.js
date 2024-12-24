import React, { useEffect, useState } from 'react';
import { useLocation, useParams, useNavigate } from 'react-router-dom';
import axios from 'axios';
import "../styles/style_Room.css";
import Invite from './Invite'

export default function Room() {
    const { roomId } = useParams();
    const location = useLocation();
    const navigate = useNavigate();

    const [roomSettings, setRoomSettings] = useState({
        roomName: location.state?.name || '',
        maxPlayers: 4,
        startingAmount: location.state?.init_score || 0,
        gameTime: location.state?.gameTime || 0,
        isPrivate: location.state?.is_private || false,
        playersInvited: [],
    });

    const [error, setError] = useState('');
    const [countdown, setCountdown] = useState(5);
    const [isCounting, setIsCounting] = useState(false);
    const [showInviteModal, setShowInviteModal] = useState(false);
    const [showExitConfirm, setShowExitConfirm] = useState(false);

    const handleChange = (e) => {
        const { name, value, type, checked } = e.target;
        setRoomSettings((prevSettings) => ({
            ...prevSettings,
            [name]: type === 'checkbox' ? checked : value,
        }));
    };

    const handlePlayerCountChange = (e) => {
        const value = Math.min(4, Math.max(2, e.target.value)); 
        setRoomSettings((prevSettings) => ({
            ...prevSettings,
            maxPlayers: value,
        }));
    };

    const handleInvitePlayer = (player) => {
        if (!roomSettings.playersInvited.includes(player.id) && roomSettings.playersInvited.length < roomSettings.maxPlayers - 1) {
            setRoomSettings((prevState) => ({
                ...prevState,
                playersInvited: [...prevState.playersInvited, player.id],
            }));
        }
        setShowInviteModal(false);
    };

    const toggleInviteModal = () => {
        setShowInviteModal(!showInviteModal);
    };

    const handleExit = () => {
        setShowExitConfirm(true);
    };

    const confirmExit = (option) => {
        setShowExitConfirm(false);
        if (option === "exit") {
            navigate('/');
        }
    };

    const handleStartGame = async () => {
        setError('');

        
        if (roomSettings.playersInvited.length < 1) {
            setError('Минимум 2 игрока для начала игры (включая вас).');
            return;
        }

        if (!roomSettings.roomName) {
            setError('Название комнаты обязательно.');
            return;
        }

        if (parseInt(roomSettings.startingAmount, 10) <= 0) {
            setError('Начальная сумма должна быть положительной.');
            return;
        }

        if (parseInt(roomSettings.gameTime, 10) <= 0) {
            setError('Время игры должно быть положительным.');
            return;
        }

        setIsCounting(true);
        setCountdown(5);

        const interval = setInterval(() => {
            setCountdown((prevCountdown) => {
                if (prevCountdown === 1) {
                    clearInterval(interval);
                    return 0;
                }
                return prevCountdown - 1;
            });
        }, 1000);

        
        setTimeout(async () => {
            setIsCounting(false);
            clearInterval(interval);
            try {
                const response = await axios.post('http://localhost:8000/api/room', {
                    room_name: roomSettings.roomName,
                    players: roomSettings.playersInvited,
                    starting_amount: roomSettings.startingAmount,
                    game_time: roomSettings.gameTime,
                    is_private: roomSettings.isPrivate,
                });

                if (response && response.data && response.data.id) {
                    navigate(`/room/${response.data.id}`, {
                        state: {
                            roomName: roomSettings.roomName,
                            players: roomSettings.playersInvited,
                        },
                    });
                } else {
                    setError('Ошибка при создании комнаты.');
                }
            } catch (error) {
                setError('Ошибка сервера при создании комнаты. Пожалуйста, попробуйте позже.');
            }
        }, 5000); 
    };

    return (
        <div className="room-setup">
            <div className="content_main_head">
                <h1>{roomSettings.roomName ? roomSettings.roomName : "Создание новой комнаты"}</h1>
                {error && <div className="error" style={{ color: 'red' }}>{error}</div>} {/* Ошибка отображается в красном */}
                <button className="button_exit" onClick={handleExit}>Отмена</button>
            </div>

            <form className="setup_form">
                <div className="form_group">
                    <label>Название комнаты:</label>
                    <input
                        type="text"
                        name="roomName"
                        value={roomSettings.roomName}
                        onChange={handleChange}
                        required
                    />
                </div>

                <div className="form_group">
                    <label>Максимальное количество игроков:</label>
                    <input
                        type="number"
                        name="maxPlayers"
                        value={roomSettings.maxPlayers}
                        onChange={handlePlayerCountChange}
                        min="2" 
                        max="4"
                        required
                    />
                </div>

                <div className="form_group">
                    <label>Начальная сумма:</label>
                    <input
                        type="number"
                        name="startingAmount"
                        value={roomSettings.startingAmount}
                        onChange={handleChange}
                        min="0"
                        required
                    />
                </div>

                <div className="form_group">
                    <label>Время игры (мин):</label>
                    <input
                        type="number"
                        name="gameTime"
                        value={roomSettings.gameTime}
                        onChange={handleChange}
                        min="1"
                        required
                    />
                </div>

                <div className="form_group">
                    <label>
                        <input
                            type="checkbox"
                            name="isPrivate"
                            checked={roomSettings.isPrivate}
                            onChange={handleChange}
                        />
                        Приватная комната
                    </label>
                </div>

                <button type="button" className="button_game_create" onClick={handleStartGame}>Создать игру</button>
            </form>

            <div className="players-container">
                <h2>Игроки:</h2>
                <br/>
                <div className="player-slot">
                    <span>Администратор: Вы</span>
                </div>
                
                {roomSettings.playersInvited.map((id, index) => (
                    <div key={index} className="player-slot">
                        <span>Игрок {id}</span>
                    </div>
                ))}

                {Array.from({ length: roomSettings.maxPlayers - 1 - roomSettings.playersInvited.length }).map((_, index) => (
                    <div key={index} className="player-slot empty">
                        <span>Свободное место</span>
                        <button className="button_invite_player" onClick={toggleInviteModal}>Пригласить игрока</button>
                    </div>
                ))}
            </div>

            {showInviteModal && (
                 <Invite roomId={roomId} close={toggleInviteModal} />
            )}

            {showExitConfirm && (
                <div className="modal">
                    <div className="modal_content">
                        <h2>Подтвердите действие</h2>
                        <p>Вы уверены, что хотите отменить создание комнаты?</p>
                        <button className="button_exit" onClick={() => confirmExit("exit")}>В главное меню</button>
                        <button className="button_exit" onClick={() => confirmExit("continue")}>Продолжить создание комнаты</button>
                    </div>
                </div>
            )}

            {isCounting && (
                <div>
                    <h2 className="countdown">Обратный отсчет: {countdown}</h2>
                </div>
            )}
        </div>
    );
}

export { Room };