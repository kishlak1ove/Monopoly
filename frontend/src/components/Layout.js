import React from 'react'
import header_logo2 from "../employ/header_logo2.png"
import footer_icon from "../employ/footer_icon.png"
import vk_footer from "../employ/vk_footer.png"
import telegram_footer from "../employ/telegram_footer.png"
import discord_footer from "../employ/discord_footer.png"
import { Link, Outlet } from "react-router-dom"
import "../styles/style_Layout.css"
import player_img from "../employ/player_icon.png"
import { useAuth } from './AuthContext';
export default function Layout() {
    const { auth, logout } = useAuth();
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
                      <Link class="header_button_" to="/search">Поиск игр</Link>
                      <Link class="header_button_" to="/room/:roomId">Создать игру</Link>
                      <Link class="header_button" to="/shop">Магазин</Link>
                      <Link class="header_button" to="/achiev">Достижения</Link>
                      <Link class="img_player" to="/playerprof"><img src={player_img} width="40px" height="40px" alt="player_profile"></img></Link>
                  </div>
                  <div class="login_button_header">
                    {auth.isLoggedIn ? (
                            <button className="header_button_" onClick={logout}>Выйти</button> 
                        ) : (
                            <Link className="header_button_" to="/login">Войти</Link> 
                    )}
                  </div>
              </div>
          </div>
      </header>


      <Outlet />

      <footer>
              <div class="container_footer">
                  <div class="line_footer">
                      <div class="logo_footer">
                          <img src={footer_icon} width="70" height="70" alt="footer"/>
                          <h5 class="name_logo_footer">Монополия — бесплатная онлайн-игра.</h5>
                      </div>

                      <div class="container_links_footer">
                          <h3>Материалы</h3>
                          <div class="links_footer_list">
                              <ul class="links_list_">
                                  <li><Link class="link_widgets_footer" to="">Правила сайта</Link></li>
                                  <li><Link class="link_widgets_footer" to="">Как тут играть</Link></li>
                                  <li><Link class="link_widgets_footer" to="">О нарушениях</Link></li>
                                  <li><Link class="link_widgets_footer" to="">О магазине</Link></li>
                                  <li><Link class="link_widgets_footer" to="">Об инвентаре</Link></li>
                              </ul>
                              <ul class="links_list_">
                                  <li><Link class="link_widgets_footer" to="">О достижениях</Link></li>
                                  <li><Link class="link_widgets_footer" to="">Документация</Link></li>
                                  <li><Link class="link_widgets_footer" to="">Статус сайта</Link></li>
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