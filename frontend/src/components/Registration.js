import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import "../styles/style_Registr.css"; 
import axios from 'axios';

export default function Registration() {
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [passwordMore, setPasswordMore] = useState('');
    const [message, setMessage] = useState('');
    const [errors, setErrors] = useState({});

    const handleRegister = async (e) => {
        e.preventDefault();
        setMessage('');
        setErrors({});

        if (!username){
            setErrors((prev) => ({ ...prev, username: '*Пустое поле "Имя пользователя"' }));
            return
        }

        if (!email) {
        setErrors((prev) => ({ ...prev, email: '*Пустое поле "Электронная почта"' }));
        return;
        }

        const cyrillicPattern = /[А-Яа-яЁё]/;
        if (cyrillicPattern.test(email)) {
            setErrors((prev) => ({ ...prev, email: '*Электронная почта не должна содержать кириллицу.' }));
            return;
        } 

        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailPattern.test(email)) {
            setErrors((prev) => ({ ...prev, email: '*Некорректный формат электронной почты' }));
            return;
        }

        if (!password) {
            setErrors((prev) => ({ ...prev, password: '*Пустое поле "Пароль"' }));
            return;
        }

        if (cyrillicPattern.test(password)) {
        setErrors((prev) => ({ ...prev, password: '*Пароль не должен содержать кириллицу.' }));
        return;
        }

        if (password.length < 8) {
            setErrors((prev) => ({ ...prev, password: "*Пароль должен содержать не менее 8 символов." }));
            return;
        }

        if (!passwordMore) {
        setErrors((prev) => ({ ...prev, passwordMore: '*Пустое поле "Повтор пароля"' }));
        return;
        }

        
        if (password !== passwordMore) {
            setErrors((prev) => ({ ...prev, passwordMore: '*Пароли не совпадают' }));
            return;
        }

        try {
            const response = await axios.post('http://localhost:8000/api/register/', {
                username,
                email,
                password,
                password_more: passwordMore,
            });

            setMessage('Регистрация успешна! Теперь вы можете войти.');
            setUsername('');
            setEmail('');
            setPassword('');
            setPasswordMore('');

        } catch (error) {
            if (error.response && error.response.data) {
                if (error.response.data.username) {
                    setErrors((prev) => ({ ...prev, username: error.response.data.username[0] }));
                }
                if (error.response.data.email) {
                    setErrors((prev) => ({ ...prev, email: error.response.data.email[0] }));
                }
                if (error.response.data.password) {
                    setErrors((prev) => ({ ...prev, password: error.response.data.password[0] }));
                }
                setMessage('Ошибка регистрации: ' + error.response.data.detail);
            } else {
                setMessage('Ошибка регистрации');
            }
        }
    };

    return (
        <div className="fake_body_reg">
            <div className="main_container">
                <h1 className="registr_text">Регистрация</h1>
                <form onSubmit={handleRegister}>
                    <label htmlFor="username"><b>Имя пользователя</b></label>
                    {errors.username && <span style={{ color: "red" }}>{errors.username}</span>}
                    <input className="input_email" type="text" placeholder="Введите имя пользователя" value={username} onChange={(e) => setUsername(e.target.value)} required />

                    <label htmlFor="email"><b>Электронная почта</b></label>
                    {errors.email && <span style={{color: "red"}}>{errors.email}</span>}
                    <input className="input_email" type="email" placeholder="Введите электронную почту" value={email} onChange={(e) => setEmail(e.target.value)} required />

                    <label htmlFor="password"><b>Пароль</b></label>
                    {errors.password && <span style={{color: "red"}}>{errors.password}</span>}
                    <input className="input_password" type="password" placeholder="Введите пароль" value={password} onChange={(e) => setPassword(e.target.value)} required />

                    <label htmlFor="password_more"><b>Повторите пароль</b></label>
                    {errors.passwordMore && <span style={{color: "red"}}>{errors.passwordMore}</span>}
                    <input className="input_more_psw" type="password" placeholder="Введите пароль ещё раз" value={passwordMore} onChange={(e) => setPasswordMore(e.target.value)} required />

                    <div className="container_reg_button">
                        <button type="submit" className="registr_button">Регистрация</button>
                    </div>
                    <span className="error_django" style={{ color: "red" }}>{message}</span>
                </form>
                <div className="container_sign">
                    <p>
                        Уже были зарегистрированы?
                        <Link className="link_entrance" to="/login"> Войти</Link>
                    </p>
                </div>
            </div>
        </div>
    );
}

export { Registration }
