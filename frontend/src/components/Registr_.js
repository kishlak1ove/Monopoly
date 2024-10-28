import React from 'react'
import { Link } from 'react-router-dom'
import "./style_Registr.css"

export default function Registr_() {
  return (
<div class="fake_body_reg">
  <div class="container">
    <div class="main_container">
        <div class="container_logo">
            <h1 class="registr_text">Регистрация</h1>
        </div>
        <p>Пожалуйста, заполните поля ниже, чтобы создать учетную запись.</p>
        <hr />
        <label for="email"><b>Электронная почта</b></label>
        <input class="input_email" type="email" placeholder="Введите электронную почту" name="email" required />
        <label for="password"><b>Пароль</b></label>
        <input class="input_password" type="password" placeholder="Введите пароль" name="passwrod" required />
        <label for="password_more"><b>Повторите пароль</b></label>
        <input class="input_more_psw" type="password" placeholder="Введите пароль ещё раз" name="passwrod_more" required />
        <br />
        <div class="container_reg_button">
        <button type="sumbit" class="registr_button">Регистрация</button>
        </div>
        <div class="container_sign">
            <p>
                Уже были зарегистрированы?
                <Link class="link_entrance" to="/login" > Войти</Link>
            </p>	
        </div>
    </div>
  </div>
</div>
  )
}

export { Registr_ }
