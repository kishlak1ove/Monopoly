import React from 'react'

export default function login() {
  return (
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
        <input class="input_password" type="text" placeholder="Введите пароль" name="passwrod" required />
        <label for="password_more"><b>Повторите пароль</b></label>
        <input class="input_more_psw" type="text" placeholder="Введите пароль ещё раз" name="passwrod_more" required />
        <br />
        <div class="container_reg_button">
        <button type="sumbit" class="registr_button">Регистрация</button>
        </div>
        <div class="container_sign">
            <p>
                Уже были зарегистрированы?
            </p>	
        </div>
    </div>
</div>
  )
}
