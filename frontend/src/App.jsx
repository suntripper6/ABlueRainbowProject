import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import Home from './components/Home';
import Feedback from './components/Feedback';
import FacilityDetail from './components/FacilityDetail';
import AssistedLivingList from './components/AssistedLivingList';
import HomeHealthList from './components/HomeHealthList';
import SkilledNursingList from './components/SkilledNursingList';
import HospiceList from './components/HospiceList';
import { getAssistedLivingDetail, getHomeHealthDetail, getSkilledNursingDetail, getHospiceDetail } from './api';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import './abr.css';

function App() {
  return (
    <Router>
      <div className="site-chrome d-flex flex-column min-vh-100">
        <Header />

        <main className="app-main flex-grow-1">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/assistedliving" element={<AssistedLivingList />} />
            <Route path="/assistedliving/:id" element={<FacilityDetail kicker="Assisted Living" fetchData={getAssistedLivingDetail} />} />
            <Route path="/homehealth" element={<HomeHealthList />} />
            <Route path="/homehealth/:id" element={<FacilityDetail kicker="Home Health" fetchData={getHomeHealthDetail} />} />
            <Route path="/skillednursing" element={<SkilledNursingList />} />
            <Route path="/skillednursing/:id" element={<FacilityDetail kicker="Skilled Nursing" fetchData={getSkilledNursingDetail} />} />
            <Route path="/hospice" element={<HospiceList />} />
            <Route path="/hospice/:id" element={<FacilityDetail kicker="Hospice Care" fetchData={getHospiceDetail} />} />
            <Route path="/feedback" element={<Feedback />} />
          </Routes>
        </main>

        <footer className="site-footer">
          <div className="footer-panel text-center text-lg-start d-flex flex-column flex-lg-row justify-content-between gap-2">
            <div><strong>A Blue Rainbow</strong> helps families compare care options with a calmer, clearer experience.</div>
            <div>&copy; {new Date().getFullYear()} A Blue Rainbow</div>
          </div>
        </footer>
      </div>
    </Router>
  );
}

export default App;
