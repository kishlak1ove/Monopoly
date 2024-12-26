import React, { useState } from "react";
import { Link } from 'react-router-dom';
import "../styles/style_Login.css"; 
import axios from 'axios';
import { useAuth  } from './AuthContext';

export default function Login_() {
    const { login } = useAuth(); 
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [message, setMessage] = useState('');
    const [errors, setErrors] = useState({});

    const handleLogin = async (e) => {
        e.preventDefault();
        setMessage('');
        setErrors({});

        if (!username) {
            setErrors((prev) => ({ ...prev, username: '*Поле "Имя пользователя" обязательно' }));
            return;
        }

        if (!password) {
            setErrors((prev) => ({ ...prev, password: '*Поле "Пароль" обязательно' }));
            return;
        }

        try {
            const response = await axios.post('http://localhost:8000/api/login/', {
                username,
                password
            });

            localStorage.setItem('access_token', response.data.access_token);
            localStorage.setItem('refresh_token', response.data.refresh_token);
            localStorage.setItem('user_id', response.data.user_id);
            localStorage.setItem('username', response.data.username);

            login({
                id: response.data.user_id,
                username: response.data.username,
            });

            setMessage('Вход успешен!');
            setUsername('');
            setPassword('');
        } catch (error) {
            setMessage('Ошибка входа: ' + error.response?.data?.message || 'Неверные учетные данные');
        }
    };

    return (
        <div className="fake_body_log">
            <div className="main_container_log">
                <h1 className="login_text">Авторизация</h1>
                <form onSubmit={handleLogin}>
                    <label htmlFor="username"><b>Имя пользователя</b></label>
                    {errors.username && <span style={{ color: "red" }}>{errors.username}</span>}
                    <input className="input_email_log" type="text" placeholder="Введите имя пользователя" value={username} onChange={(e) => setUsername(e.target.value)} required />

                    <label htmlFor="password"><b>Пароль</b></label>
                    {errors.password && <span style={{ color: "red" }}>{errors.password}</span>}
                    <input className="input_password_log" type="password" placeholder="Введите пароль" value={password} onChange={(e) => setPassword(e.target.value)} required />

                    <div className="container_log_button">
                        <button type="submit" className="login_button">Войти</button>
                    </div>
                    <span className="error_django" style={{ color: "red" }}>{message}</span>
                </form>
                <div className="container_sign">
                    <p>
                        <Link className="link_entrance" to="/login/passforg">Забыли пароль?</Link>
                    </p>
                    <p>
                        Ещё не были зарегистрированы?
                        <Link className="link_entrance" to="/register"> Зарегистрироваться</Link>
                    </p>
                </div>
            </div>
        </div>
    );
}

export { Login_ }