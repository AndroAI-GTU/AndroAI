"use client"

import { useState, useRef, useEffect } from "react";
import { Link } from "react-router-dom";
import './SignUp.css';

export default function Component() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [isNameValid, setIsNameValid] = useState(true);
  const [isEmailValid, setIsEmailValid] = useState(true);
  const [isPasswordValid, setIsPasswordValid] = useState(true);
  const nameInputRef = useRef(null);
  const emailInputRef = useRef(null);
  const passwordInputRef = useRef(null);

  useEffect(() => {
    nameInputRef.current.focus();
  }, []);

  const handleNameChange = (e) => {
    const value = e.target.value.trim();
    setName(value);
    setIsNameValid(value.length >= 3);
  };

  const handleEmailChange = (e) => {
    const value = e.target.value.trim();
    setEmail(value);
    setIsEmailValid(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(value));
  };

  const handlePasswordChange = (e) => {
    const value = e.target.value;
    setPassword(value);
    setIsPasswordValid(value.length >= 8);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (isNameValid && isEmailValid && isPasswordValid) {
      console.log("Form submitted:", { name, email, password });
    } else {
      if (!isNameValid) {
        nameInputRef.current.focus();
      } else if (!isEmailValid) {
        emailInputRef.current.focus();
      } else if (!isPasswordValid) {
        passwordInputRef.current.focus();
      }
    }
  };

  return (
    <div className="signup-container">
      <div className="signup-overlay"></div>
      <div className="signup-content">
        <h1 className="signup-title">Sign Up</h1>
        <form onSubmit={handleSubmit} className="signup-form">
          <div className="signup-input-container">
            <label htmlFor="name" className="signup-label">Name</label>
            <input
              ref={nameInputRef}
              type="text"
              id="name"
              value={name}
              onChange={handleNameChange}
              className={`signup-input ${!isNameValid ? "signup-input-invalid" : "signup-input-valid"}`}
              placeholder="John Doe"
            />
            {!isNameValid && <p className="signup-error">Name must be at least 3 characters long.</p>}
          </div>
          <div className="signup-input-container">
            <label htmlFor="email" className="signup-label">Email address</label>
            <input
              ref={emailInputRef}
              type="email"
              id="email"
              value={email}
              onChange={handleEmailChange}
              className={`signup-input ${!isEmailValid ? "signup-input-invalid" : "signup-input-valid"}`}
              placeholder="you@example.com"
            />
            {!isEmailValid && <p className="signup-error">Please enter a valid email address.</p>}
          </div>
          <div className="signup-input-container">
            <label htmlFor="password" className="signup-label">Password</label>
            <input
              ref={passwordInputRef}
              type="password"
              id="password"
              value={password}
              onChange={handlePasswordChange}
              className={`signup-input ${!isPasswordValid ? "signup-input-invalid" : "signup-input-valid"}`}
              placeholder="********"
            />
            {!isPasswordValid && <p className="signup-error">Password must be at least 8 characters long.</p>}
          </div>
          <button type="submit" className="signup-button">
            Sign up
          </button>
        </form>
        <div className="signup-footer">
          Already have an account?{" "}
          <Link to="/login" className="signup-link" prefetch={false}>
            Login
          </Link>
        </div>
      </div>
    </div>
  );
}
