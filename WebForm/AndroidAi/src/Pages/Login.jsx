"use client"

import { useState, useEffect } from "react";
import './Login.css'; 

export default function Component() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  useEffect(() => {}, []);
  
  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Login:", { name, email, password });
  };

  return (
    <div className="login-container">
      <div className="login-overlay" />
      <div className="login-content">
        <h1 className="login-title">Login</h1>
        <form onSubmit={handleSubmit} className="login-form">
          <div>
            <label htmlFor="name" className="login-label">Name</label>
            <div className="login-input-container">
              <input
                id="name"
                name="name"
                type="text"
                autoComplete="name"
                required
                className="login-input"
                placeholder="John Doe"
                value={name}
                onChange={(e) => setName(e.target.value)}
              />
            </div>
          </div>
          <div>
            <label htmlFor="email" className="login-label">Email address</label>
            <div className="login-input-container">
              <input
                id="email"
                name="email"
                type="email"
                autoComplete="email"
                required
                className="login-input"
                placeholder="you@example.com"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
              />
            </div>
          </div>
          <div>
            <label htmlFor="password" className="login-label">Password</label>
            <div className="login-input-container">
              <input
                id="password"
                name="password"
                type="password"
                autoComplete="current-password"
                required
                className="login-input"
                placeholder="********"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
            </div>
          </div>
          <div>
            <button
              type="submit"
              className="login-button"
            >
              Login
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
