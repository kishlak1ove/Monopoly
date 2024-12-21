import React, { useState } from 'react';
import { Link } from 'react-router-dom'
import "../styles/style_Registr.css"
import axios from 'axios';

export default function Registr_() {

  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [passwordMore, setPasswordMore] = useState('');
  const [message, setMessage] = useState('');
  const [errors, setErrors] = useState({});

  const handleRegister = async (e) => {
      e.preventDefault();
      setMessage('');
      setErrors({});

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
        const response = await axios.post('http://127.0.0.1:8000/api/register/', {
            email,
            password,
            password_more: passwordMore,
        });
        setMessage('Регистрация успешна!');
        setEmail('');
        setPassword('');
        setPasswordMore('');
      } catch (error) {
        if (error.response && error.response.data) {
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
<div class="fake_body_reg">
    <div class="main_container">
        <div class="container_logo">
            <h1 class="registr_text">Регистрация</h1>
        </div>
        <p>Пожалуйста, заполните поля ниже, чтобы создать учетную запись.</p>
        <hr />
        <form onSubmit={handleRegister}>
        <label for="email"><b>Электронная почта</b></label>
        {errors.email && <span style={{color: "red"}}>{errors.email}</span>}
        <input class="input_email" type="email" placeholder="Введите электронную почту" value={email} onChange={(e) => setEmail(e.target.value)} required />
        <label for="password"><b>Пароль</b></label>
        {errors.password  && <span style={{color: "red"}}>{errors.password }</span>}
        <input class="input_password" type="password" placeholder="Введите пароль" name="passwrod" value={password} onChange={(e) => setPassword(e.target.value)}  required />
        <label for="password_more"><b>Повторите пароль</b></label>
        {errors.passwordMore  && <span style={{color: "red"}}>{errors.passwordMore }</span>}
        <input class="input_more_psw" type="password" placeholder="Введите пароль ещё раз" name="passwrod_more" value={passwordMore} onChange={(e) => setPasswordMore(e.target.value)} required />
        <br />
        <div class="container_reg_button">
        <button type="submit" class="registr_button">Регистрация</button>
        </div>
        </form>
        <span className="error_django" style={{color: "red"}}>{message}</span>
        <div class="container_sign">
            <p>
                Уже были зарегистрированы?
                <Link class="link_entrance" to="/login" > Войти</Link>
            </p>
        </div>
    </div>
</div>
  )
}

export { Registr_ }
