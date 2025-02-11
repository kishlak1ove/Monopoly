import React from 'react';
import main_logo from "../employ/main_logo.png";
import achiev_main from "../employ/achiev_main.png";
import collect_main from "../employ/collect_main.png";
import competitions_main from "../employ/competitions_main.png";
import free_main from "../employ/free_main.png";
import friends_main from "../employ/friends_main.png";
import modes_main from "../employ/modes_main.png";
import planet_main from "../employ/planet_main.png";
import "../styles/style_Main.css"
import { Link } from "react-router-dom"

export default function Main() {
  return (
    <main>  
        <div class="container_main">
            <div class="content_main">
                <br></br>
                <div class="content_main_head">
                    <h1>Приглашаем в Монополию.</h1>
                    <h2>Это отличное место, чтобы поиграть с друзьями в легендарную настольную игру.</h2>
                    <a class="button_game_main" href="/login">Начать игру</a>
                </div>
                <div class="img_main_center">
                    <img class="img_main_logo" src={main_logo} width = "373" height="459" alt="Логотип" />
                </div>
                <div class="content_main_footer">
                    <h1 class="name_main_footer">Почему вам понравится играть у нас?</h1>
                    <div class="list_container_cards">
                        <div class="card_container">
                            <img class="img_container_main" src={free_main} width="180" height="180" alt="Бесплатно" />
                            <h2>Это бесплатно!</h2>
                            <div>Просто <Link to="">создайте аккаунт</Link> и начните играть — никаких подписок и платежей.</div>
                        </div>
                        <div class="card_container">
                            <img class="img_container_main" src={modes_main} width="180" height="180" alt="Режимы" />
                            <h2>Множество режимов</h2>
                            <div>Мы создали множество режимов с уникальными механиками, в которых вы всегда испытаете что-то новое.</div>
                            <br />
                            <div>А классические правила были улучшены, чтобы было интереснее играть в онлайне.</div>
                        </div>
                        <div class="card_container">
                            <img class="img_container_main" src={competitions_main} width="180" height="180" alt="Соревнования" />
                            <h2>Соревнования</h2>
                            <div>Играйте в Соревновательном режиме, чтобы получить звание и поднимать его с каждой победой.</div>
                        </div>
                        <div class="card_container">
                            <img class="img_container_main" src={friends_main} width="180" height="180" alt="Друзья" />
                            <h2>Новые друзья</h2>
                            <div>Находите интересных вам игроков и добавляйте их в друзья. Общайтесь в личных сообщениях, обсуждая новые тактики — ну или делитесь новыми мемами.</div>
                        </div>
                        <div class="card_container">
                            <img class="img_container_main" src={collect_main} width="180" height="180" alt="Коллекционирование" />
                            <h2>Коллекционирование</h2>
                            <div>У нас имеется множество <Link to="*">предметов</Link>, некоторые из которых очень редкие. Соберите себе коллекцию из того, что вам больше нравится!</div>
                        </div>
                        <div class="card_container">
                            <img class="img_container_main" src={planet_main} width="180" height="180" alt="Играть везде" />
                            <h2>Играйте где угодно</h2>
                            <div>Вы можете играть на любом устройстве, где есть браузер — хоть на компьютере из дома, хоть на телефоне, пока едете в метро.</div>
                        </div>
                        <div class="card_container">
                            <img class="img_container_main" src={achiev_main} width="180" height="180" alt="Достижения" />
                            <h2>Получайте доостижения</h2>
                            <div>Вы можете получать достижения, за которые вам выплачивается награда.</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </main>
  )
}

export { Main }