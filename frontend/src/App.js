import { Main } from "./components/Main"
import { Notfound } from "./components/Notfound"
import './App.css';
import { Routes, Route} from 'react-router-dom';
import { Login } from "./components/Login"
import { Registr } from "./components/Registr"
import { Layout } from "./components/Layout"

function App() {
  return (
  <>
    <div className="App">
    <Routes>
      <Route path="/" element={<Layout />}>
        <Route index element={<Main />} />
        <Route path='login' element={<Login />} />
        <Route path='registr' element={<Registr />} />
        <Route path='*' element={<Notfound />} />
      </Route>
    </Routes>
    </div>
  </>
  );
}

export default App;
