import React from 'react';
import { useLocation } from 'react-router-dom';
import Header from './components/Header';
import Question from './components/Question';
import { Outlet } from 'react-router-dom';
import './App.css';

const App = () => {
  const location = useLocation();

  return (
    <>
      <Header />
      <Outlet />
      {location.pathname === '/' && <Question />}
    </>
  );
};

export default App;
