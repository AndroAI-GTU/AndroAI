import React from 'react';
import { Link } from "react-router-dom";

const Header = () => {
  return (
    <nav className='navbar'>
      <Link to="/" className='site-title'>AndroidAi</Link>
      <ul className='navbar-mid'>
        <li><Link to="/about">About</Link></li>
        <li><Link to="/contact">Contact</Link></li>
      </ul>
      <ul className='navbar-button'>
        <li>
          <Link to="/login" className='button-link'>
            <i className="fa-solid fa-right-to-bracket"></i> Login
          </Link>
        </li>
        <li>
          <Link to="/signup" className='button-link'>
            <i className="fa-solid fa-user" style={{ marginRight: '0.5rem' }}></i> Sign Up
          </Link>
        </li>
      </ul>
    </nav>
  );
};

export default Header;
