import { useState } from 'react';
import { useNavigate } from 'react-router-dom';

export default function useLoading() {
    const [loading, setLoading] = useState(false);
    const navigate = useNavigate();

    const navigateWithLoader = (path, delay = 500) => {
        setLoading(true);

        setTimeout(() => {
            navigate(path);
            setLoading(false); 
        }, delay);
    };
    return { loading, navigateWithLoader };
}

export { useLoading }