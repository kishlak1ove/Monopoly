import React, { useState } from 'react';
import axios from 'axios';


const Invite = ({ roomId, close }) => {
    const [userId, setUserId] = useState('');
    const [message, setMessage] = useState('');
    const [error, setError] = useState('');

    const handleSendInvite = async () => {
        setMessage('');
        setError('');

        if (!userId) {
            setError('Пожалуйста, введите ID пользователя.');
            return;
        }

        try {
            const response = await axios.post('http://localhost:8000/api/invite', {
                room: roomId,
                user: userId,
            });

            if (response.status === 201) {
                setMessage('Приглашение отправлено!');
                setUserId(''); 
            } else {
                setError('Ошибка при отправке приглашения. Попробуйте еще раз.');
            }
        } catch (error) {
            console.error('Ошибка при отправке приглашения:', error);
            if (error.response && error.response.data) {
                setError(error.response.data.error || 'Ошибка при отправке приглашения.');
            } else {
                setError('Ошибка при отправке приглашения. Проверьте соединение.');
            }
        }
    };

    return (
        <div className="modal">
            <div className="modal_content">
                <h2>Отправить приглашение</h2>
                {message && <div style={{ color: 'green' }}>{message}</div>}
                {error && <div style={{ color: 'red' }}>{error}</div>}
                <input
                    type="text"
                    placeholder="ID пользователя"
                    value={userId}
                    onChange={(e) => setUserId(e.target.value)}
                />
                <button onClick={handleSendInvite}>Отправить приглашение</button>
                <button onClick={close}>Закрыть</button>
            </div>
        </div>
    );
};

export default Invite;