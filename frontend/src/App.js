import { Main } from "./components/Main"
import { Notfound } from "./components/Notfound"
import './App.css';
import { Routes, Route} from 'react-router-dom';
import { Login_ } from "./components/Login_"
import { Registr_ } from "./components/Registr_"
import { Layout } from "./components/Layout"

function App() {
  return (
  <>
    <div className="App">
    <Routes>
      <Route path="/" element={<Layout />}>
        <Route index element={<Main />} />
        <Route path='login' element={<Login_ />} />
        <Route path='registr' element={<Registr_ />} />
        <Route path='*' element={<Notfound />} />
      </Route>
    </Routes>
    </div>
  </>
  );
}

export default App;
