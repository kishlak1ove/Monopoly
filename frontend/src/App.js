import { Main } from "./components/Main";
import { Notfound } from "./components/Notfound"; 
import './App.css';
import { Routes, Route } from 'react-router-dom';
import { Login_ } from "./components/Login_";
import { Registr_ } from "./components/Registr_";
import { Create } from "./components/Create";
import { Layout } from "./components/Layout";
import { Shop } from "./components/Shop"
import { Achievements } from "./components/Achievements"
import { Player } from "./components/Player"
import { Room } from "./components/Room"
import { Game } from "./components/Game"

function App() {

  return (
  <>
    <div className="App">
        <Routes>
          <Route path="/" element={<Layout />}>
              <Route index element={<Main />} />
              <Route path='login' element={<Login_ />} />
              <Route path='registr' element={<Registr_ />} />
              <Route path='create' element={<Create />} />
              <Route path='shop' element={<Shop />} />
              <Route path='achiev' element={<Achievements />} />
              <Route path='player' element={<Player />} />
              <Route path='*' element={<Notfound />} />
              <Route path='room/:roomId/game' element={<Game />} />
              <Route path='room/:roomId' element={<Room />} />
          </Route>
        </Routes>
    </div>
  </>
  );
}

export default App;
