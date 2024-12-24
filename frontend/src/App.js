import { Main } from "./components/Main";
import { Notfound } from "./components/Notfound"; 
import './App.css';
import { Routes, Route } from 'react-router-dom';
import { Login_ } from "./components/Login_";
import { Registr_ } from "./components/Registr_";
import { Layout } from "./components/Layout";
import { Shop } from "./components/Shop"
import { Achievements } from "./components/Achievements"
import { PlayerProfile } from "./components/PlayerProfile"
import { Room } from "./components/Room"
import { Game } from "./components/Game"
import { Search } from "./components/Search"
import { ForgPass } from "./components/ForgPass"

function App() {

  return (
  <>
    <div className="App">
        <Routes>
          <Route path="/" element={<Layout />}>
              <Route index element={<Main />} />
              <Route path='login' element={<Login_ />} />
              <Route path='register' element={<Registr_ />} />
              <Route path='shop' element={<Shop />} />
              <Route path='achiev' element={<Achievements />} />
              <Route path='playerprof' element={<PlayerProfile />} />
              <Route path='*' element={<Notfound />} />
              <Route path='room/:roomId' element={<Room />} />
              <Route path='room/:roomId/game' element={<Game />} />
              <Route path='search' element={<Search />} />
              <Route path='login/passforg' element={<ForgPass />} />
          </Route>
        </Routes>
    </div>
  </>
  );
}

export default App;
