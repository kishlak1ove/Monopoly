import React, { useState } from 'react';
import one_img from "./1.png"
import two_img from "./2.png"
import three_img from "./3.png"
import "./style_Slider.css"

export default function Slider() {

  const images = [
    { id: 1, src: one_img, alt: 'Image 1' },
    { id: 2, src: two_img, alt: 'Image 2' },
    { id: 3, src: three_img, alt: 'Image 3' },
  ];

  const [currentIndex, setCurrentIndex] = useState(0);

  const nextSlide = () => {
      setCurrentIndex((prevIndex) => (prevIndex + 1) % images.length);
  };

  const prevSlide = () => {
      setCurrentIndex((prevIndex) => (prevIndex - 1 + images.length) % images.length);
  };

  return (
  <div className="slider">
      <button className="arrow left" onClick={prevSlide}>&#10094;</button>
      <div className="slider-container">
          <img src={images[currentIndex].src} alt={images[currentIndex].alt} className="slider-image" />
      </div>
      <button className="arrow right" onClick={nextSlide}>&#10095;</button>
  </div>
  )
}

export { Slider }