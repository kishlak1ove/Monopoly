import React from 'react'
import "../styles/style_Achiev.css"
import ProgressBar from "../progress/Progress_bar"

export default function Achievements() {

    const achievements = [
        { label: "Собрать 500 долларов", current: 350, max: 500, amount: 50 },
        { label: "Прокатиться 10 раз по полю", current: 8, max: 10, amount: 100 },
        { label: "Купить 5 свойств", current: 3, max: 5, amount: 150 },
        { label: "Построить 3 отеля", current: 1, max: 3, amount: 250 },
        { label: "Выйти из тюрьмы 5 раз", current: 2, max: 5, amount: 100 }
    ];

  return (
    <div className='fake_body_achiev'>
        <br></br>
        <div class="content_main_head">
            <div class="shop_name_header">
                <h1>Достижения</h1>
            </div>
            <div class="shop_info_header">
                <h2>Зарабатывайте монеты на достижениях, открывая их.</h2>
            </div>
        </div>
        <div class="container_achiev">
            <div class="list_card_achiev">
                <div>
                    {achievements.map((achievement, index) => (
                        <ProgressBar
                            key={index}
                            current={achievement.current}
                            max={achievement.max}
                            label={achievement.label}
                            amount={achievement.amount} />
                    ))}
                </div>
            </div>
        </div>
    </div>
  )
}

export { Achievements }
