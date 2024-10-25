import React from 'react'

export default function Validation(values) {
        let errors = { }
    
   
        if(!values.email){
            errors.email = ` *Пустое поле "Электронная почта"`
        }
        else if(values.email.length < 6 || values.email.length > 50){
            errors.email = " *Длина адреса должна быть больше 6 символов"  
        }

        if(!values.password){
            errors.password = ` *Пустое поле "Пароль"`
        }
        else if(values.password.length < 8){
            errors.password = " *Длина пароля должна быть больше 8 символов"  
        }

        return errors
    }

export {Validation}
