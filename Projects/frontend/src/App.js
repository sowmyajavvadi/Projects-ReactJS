// import logo from './logo.svg';
import './App.css';
import React from 'react';
import LoginForm from './pages/LoginForm.jsx';
import SideMenuBar from '/Users/sowmyajavvadi/Projects/frontend/src/Components/SideMenuBar/SideMenuBar.jsx';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import VehicleDetails from './pages/VehicleDetails.jsx';
import VehicleInstallments from './pages/VehicleInstallments.jsx';
import GarageExpenses from './pages/GarageExpenses.jsx';
import EmployeeDetails from './pages/EmployeeDetails.jsx';
import TrafficFines from './pages/TrafficFines.jsx';
import SupplierDetails from './pages/SupplierDetails.jsx';
import ClientPaymentDetails from './pages/ClientPaymentDetails.jsx';

function App() {
  return (
    
    <BrowserRouter className='MainContainer'>
    <SideMenuBar>
    <Routes>
      <Route path="/"element={<LoginForm/>} />
      <Route path='/VehicleDetails'element={<VehicleDetails/>} />
      <Route path='/VehicleInstallments'element={<VehicleInstallments/>} />
      <Route path='/GarageExpenses'element={<GarageExpenses/>} />
      <Route path='/EmployeeDetails'element={<EmployeeDetails/>} />
      <Route path='/TrafficFines'element={<TrafficFines/>} />
      <Route path='/SupplierDetails'element={<SupplierDetails/>} />
      <Route path='/ClientPaymentDetails'element={<ClientPaymentDetails/>} />
    
    </Routes>
    </SideMenuBar>
    </BrowserRouter>
  
  );
}

export default App;


