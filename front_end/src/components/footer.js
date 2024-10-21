import React from 'react'
import footer_icon from "./src/components_/footer_icon.png"
import vk_footer from "./src/components_/vk_footer.png"
import telegram_footer from "./src/components_/telegram_footer.png"
import discord_footer from "./src/components_/discord_footer.png"


export default function Footer() {
  return (
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
                    <img src={vk_footer} width="30" height="30" alt="Вконтакте" />
                    <img src={telegram_footer} width="30" height="30" alt="Телеграмм" />
                    <img src={discord_footer} width="30" height="30" alt="Дискорд" />
                </div>
                <h5 class="footer_text_end">Подписывайтесь на Монополию в соцсетях, чтобы быть в курсе обновлений игры.</h5>
            </div>
        </div>
    </div>
  </footer>
  )
}
