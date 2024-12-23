import React, { useState } from "react"; 
import { Link } from 'react-router-dom'
import "../styles/style_Login.css"
import axios from 'axios';



export default function Login_() {

    const [email, setEmail] = useState('');
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [token, setToken] = useState('');
    const [message, setMessage] = useState('');
    const [errors, setErrors] = useState({});

    const handleLogin = async (e) => {
        e.preventDefault();
        setMessage('');
        setErrors({});

        if (!username) {
            setErrors((prev) => ({ ...prev, username: '*Пустое поле "Имя пользователя"' }));
            return;
        }

        const cyrillicPattern = /[А-Яа-яЁё]/;
        if (cyrillicPattern.test(username)) {
            setErrors((prev) => ({ ...prev, username: '*Имя не должно содержать кириллицу.' }));
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

        try {
            const response = await axios.post('http://localhost:8000/api/login/', {
                username,
                password
            });
            setToken(response.data.token);
            setMessage('Вход успешно выполнен. Токен: ' + response.data.token);
            setUsername('');
            setPassword('');
        } catch (error) {
            if (error.response && error.response.data) {
                setMessage('Ошибка входа: ' + error.response.data.error);
            } else {
                setMessage('Ошибка входа');
            }
        }
    };


  return (
<div class="fake_body_log">
    <div class="container_log">
        <div class="main_container_log">
        <div class="container_logo">
            <h1 class="login_text">Авторизация</h1>
        </div>
        <p>Пожалуйста, заполните поля ниже, чтобы войти в учетную запись.</p>
        <hr />
        <form onSubmit={handleLogin}>
        <label htmlFor="username"><b>Имя пользователя </b></label>
        {errors.username && <span style={{ color: "red" }}>{errors.username}</span>}
        <input className="input_email_log" type="text" placeholder="Введите имя пользователя" name="username" value={username} onChange={(e) => setUsername(e.target.value)} required />
        <label htmlFor="password"><b>Пароль</b></label>
        {errors.password  && <span style={{color: "red"}}>{errors.password }</span>}
        <input className="input_password_log" type="password" placeholder="Введите пароль" name="password" value={password}  onChange={(e) => setPassword(e.target.value)}  required/>
        <br />  
        <div className="container_log_button">
        <button type="submit" className="login_button">Войти</button>
        </div>
        <span className="error_django" style={{color: "red"}}>{message}</span>
        </form>
        <div class="container_sign">
            <p>
                <Link className="link_entrance" to="/login/passforg">Забыли пароль?</Link>
            </p>
            <br></br>
            <p>
                Ещё не были зарегистрированы?
                <Link class="link_entrance" to="/registr"> Зарегестрироваться</Link>
            </p>	
        </div>
        </div>
    </div>
</div>
  )
}

export { Login_ }