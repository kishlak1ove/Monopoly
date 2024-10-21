import React from 'react';
import header_logo2 from "./components/header_logo2.png"


export default function Header() {
  return (
    <header>
    <div class="container_header">
        <div class="line_header">
            <div class="logo_header">
            <img class="img_logo_header" src={header_logo2} alt="Логотип монополии" width="144" height="114" /> 
                <div class="name_logo_header">
                    <h1 class="name_text_header">Monopoly</h1>
                </div>
            </div>
            <div class="buttons_header">
                <a class="header_button_" href="">Поиск игр</a>
                <a class="header_button" href="">Просмотр игр</a>
                <a class="header_button" href="">Магазин</a>
                <a class="header_button" href="">Достижения</a>
            </div>
            <div class="login_button_header">
                <a class="header_button_" id="log" href="">Войти</a>
            </div>
        </div>
    </div>
    </header>
  )
}
