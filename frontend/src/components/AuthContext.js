import React, { createContext, useContext, useState } from 'react';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
    const [auth, setAuth] = useState({
        isLoggedIn: false,
        user: null,
    });

    const login = (user) => {
        setAuth({ isLoggedIn: true, user });
    };

    const logout = () => {
        setAuth({ isLoggedIn: false, user: null });
        localStorage.removeItem('access_token'); // Удалите токены
        localStorage.removeItem('refresh_token');
        localStorage.removeItem('user_id');
        localStorage.removeItem('username');
    };

    return (
        <AuthContext.Provider value={{ auth, login, logout }}>
            {children}
        </AuthContext.Provider>
    );
};

export const useAuth = () => {
    return useContext(AuthContext);
};