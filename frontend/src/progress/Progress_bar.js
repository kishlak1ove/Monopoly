import React from 'react'
import "./Postgress_bar.css"
import achiev_img from "../employ/achiev_img.png"
import money from "../employ/money.png"

export default function ProgressBar({ current, max, label, amount}) {
    const percentage = (current / max) * 100;
  return (
    <>
    <div className="main_progress">
    <div className="img_achiev_container">
      <img src={achiev_img} height="100" width="100" alt="Достижение"></img>
    </div>
    <div className='main_main'>
      <div className="progress_container">
        <div className="progress_bar" style={{ width: `${percentage}%` }}>
          <span className="progress_label">{`${current} / ${max}`}</span>
        </div>
      </div>
      <div className="progress-label-text">{label}</div>
    </div>
    <div className='amount_container'>
      <div>{amount}</div>
      <img src={money} height="50" width="50" alt="монеты"></img>
    </div>
    </div>
    </>
  )
}


