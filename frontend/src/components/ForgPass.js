import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import "../styles/style_ForgPass.css"; 

export default function ForgPass() {
    const [email, setEmail] = useState('');
    const [message, setMessage] = useState('');
    const [errors, setErrors] = useState({});

    const handleForgotPassword = async (e) => {
        e.preventDefault();
        setMessage('');
        setErrors({});

        if (!email) {
            setErrors({ email: '*Пустое поле "Электронная почта"' });
            return;
        }

        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailPattern.test(email)) {
            setErrors({ email: '*Некорректный формат электронной почты' });
            return;
        }
    }

    return (
        <div className="fake_body_log">
            <div className="main_container_log">
                <div className="container_logo">
                    <h1 className="login_text">Забыли пароль?</h1>
                </div>
                <p>Введите ваш адрес электронной почты, чтобы получить ссылку для сброса пароля.</p>
                <hr />
                <form onSubmit={handleForgotPassword}>
                    <label htmlFor="email"><b>Электронная почта</b></label>
                    {errors.email && <span style={{ color: "red" }}>{errors.email}</span>}
                    <input type="email" className="input_email_log" placeholder="Введите электронную почту" value={email} onChange={(e) => setEmail(e.target.value)} required />
                    <div className="container_log_button">
                        <button type="submit" className="login_button">Отправить</button>
                    </div>
                </form>
                <span className="error_django" style={{ color: "green" }}>{message}</span>
                <div className="container_sign">
                    <p>
                        <Link className="link_entrance" to="/login">Вернуться на страницу входа</Link>
                    </p>
                </div>
            </div>
        </div>
    );
}

export { ForgPass }