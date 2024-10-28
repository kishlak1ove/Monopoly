import React, { useEffect, useState } from "react"; 
import { Link } from 'react-router-dom'
import "./style_Login.css"
import validation from './Validation'



export default function Login_() {

    const [values, setValues] = useState({
        email: "",
        password: "",
    })  

    const [errors, setError] = useState({})

    function handleChange(x){
        setValues({...values, [x.target.name]: x.target.value})
    }

    function handleSubmit(x) {
        x.preventDefault();
        setError(validation(values));
    }

    useEffect(() => {
        if(Object.keys(errors).length === 0 && (values.email !== "" && values.password !== ""))
            alert("Form submitted");
    }, [errors])


  return (
<div class="fake_body_log">
    <div class="container_log">
        <div class="main_container_log">
        <div class="container_logo">
            <h1 class="login_text">Авторизация</h1>
        </div>
        <p>Пожалуйста, заполните поля ниже, чтобы войти в учетную запись.</p>
        <hr />
        <form onSubmit={handleSubmit}>
        <label htmlFor="email"><b>Электронная почта </b></label>
        {errors.email && <span style={{color: "red"}}>{errors.email}</span>}    
        <input className="input_email_log" type="email" placeholder="Введите электронную почту" name="email" defaultValue={values.email} onChange={handleChange}/>
        <label htmlFor="password"><b>Пароль</b></label>
        {errors.password && <span style={{color: "red"}}>{errors.password}</span>}
        <input className="input_password_log" type="password" placeholder="Введите пароль" name="password" defaultValue={values.password} onChange={handleChange}/>
        <br />
        <div className="container_log_button">
        <button type="sumbit" className="login_button">Войти</button>
        </div>
        </form>
        <div class="container_sign">
            <p>
                Ещё не были зарегистрированы?
                <Link class="link_entrance" to="/registr"> Зарегестрироваться</Link>
            </p>	
        </div>
        </div>
    </div>
</div>
  )
}

export { Login_ }