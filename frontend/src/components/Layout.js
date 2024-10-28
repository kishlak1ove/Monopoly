import React from 'react'
import header_logo2 from "../components_/header_logo2.png"
import footer_icon from "../components_/footer_icon.png"
import vk_footer from "../components_/vk_footer.png"
import telegram_footer from "../components_/telegram_footer.png"
import discord_footer from "../components_/discord_footer.png"
import { Link, Outlet } from "react-router-dom"
import "./style_Layout.css"

export default function Layout() {
  return (
    <><header>
          <div class="container_header">
              <div class="line_header">
                  <div class="logo_header">
                      <img class="img_logo_header" src={header_logo2} alt="Логотип монополии" width="144" height="114" />
                      <div class="name_logo_header">
                          <Link to="/"><h1 class="name_text_header">Monopoly</h1></Link>
                      </div>
                  </div>
                  <div class="buttons_header">
                      <Link class="header_button_" to="*">Поиск игр</Link>
                      <Link class="header_button" to="*">Просмотр игр</Link>
                      <Link class="header_button" to="*">Магазин</Link>
                      <Link class="header_button" to="*">Достижения</Link>
                  </div>
                  <div class="login_button_header">
                      <Link class="header_button_" to="/login">Войти</Link>
                  </div>
              </div>
          </div>
      </header>


      <Outlet />

      <footer>
              <div class="container_footer">
                  <div class="line_footer">
                      <div class="logo_footer">
                          <img src={footer_icon} width="70" height="70" />
                          <h5 class="name_logo_footer">Монополия — бесплатная онлайн-игра.</h5>
                      </div>

                      <div class="container_links_footer">
                          <h3>Материалы</h3>
                          <div class="links_footer_list">
                              <ul class="links_list_">
                                  <li><a class="link_widgets_footer" href="">Правила сайта</a></li>
                                  <li><a class="link_widgets_footer" href="">Как тут играть</a></li>
                                  <li><a class="link_widgets_footer" href="">О нарушениях</a></li>
                                  <li><a class="link_widgets_footer" href="">О магазине</a></li>
                                  <li><a class="link_widgets_footer" href="">Об инвентаре</a></li>
                              </ul>
                              <ul class="links_list_">
                                  <li><a class="link_widgets_footer" href="">О достижениях</a></li>
                                  <li><a class="link_widgets_footer" href="">Документация</a></li>
                                  <li><a class="link_widgets_footer" href="">Статус сайта</a></li>
                              </ul>
                          </div>
                      </div>
                      <div class="container_widgets_footer">
                          <h3>Соцсети</h3>
                          <div class="list_widgets_footer">
                              <Link to="https://vk.com"><img src={vk_footer} width="30" height="30" alt="Вконтакте" /></Link>
                              <Link to="https://web.telegram.org" ><img src={telegram_footer} width="30" height="30" alt="Телеграмм" /></Link>
                              <Link to="https://discord.com"><img src={discord_footer} width="30" height="30" alt="Дискорд" /></Link>
                          </div>
                          <h5 class="footer_text_end">Подписывайтесь на Монополию в соцсетях, чтобы быть в курсе обновлений игры.</h5>
                      </div>
                  </div>
              </div>
          </footer></>
  )
}

export { Layout }