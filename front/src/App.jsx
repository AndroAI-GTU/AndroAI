import React, { useState, useEffect, useRef } from 'react';
import './App.css';
import { v4 as uuidv4 } from 'uuid'; // her kullanıcı için unique id oluşturacağız bununla

function App() 
{
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [buttons, setButtons] = useState([]);
  const [userId, setUserId] = useState(null);  // Unique ID için state
  const chatWindowRef = useRef(null);

  useEffect(() => 
  {
    // Unique ID'yi localStorage'dan kontrol et
    let storedId = localStorage.getItem('userId');

    if (!storedId) 
    {
      storedId = uuidv4();  // UUID oluştur
      localStorage.setItem('userId', storedId);
    }
    setUserId(storedId);  // State'e kaydet
  }, []);

  const sendMessage = async (message, ButtonsMessage=false) => 
  {
    if (!message || message.trim() === '') return;

    // Kullanıcı mesajını ekliyoruz
    const userMessage = { text: message, user: 'user' };

    if (!ButtonsMessage) setMessages((prevMessages) => [...prevMessages, userMessage]); // Sadece title ekrana basılıyor

    console.log("Sending message:", message);

    try 
    {
      const response = await fetch('http://localhost:5001/chat', 
      {
        method: 'POST',
        headers: 
        {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': '*',
        },
        body: JSON.stringify({ message: message, userId: userId }), // userId'yi de sunucuya gönderiyoruz
      });

      const data = await response.json();
      console.log("JSON parsed:", data);

      // Mesajın array olup olmadığını kontrol ediyoruz
      const responseData = Array.isArray(data) ? data[0] : data;

      if (responseData.text) 
      {
        const botMessage = { text: responseData.text, user: 'bot' };
        setMessages((prevMessages) => [...prevMessages, botMessage]);
      }

      // Gelen butonları kontrol ediyoruz
      if (responseData.buttons && responseData.buttons.length > 0) 
      {
        setButtons(responseData.buttons); // Butonlar varsa set ediyoruz
      } 

      else 
      {
        setButtons([]); // Butonlar yoksa sıfırlıyoruz
      }

    } 

    catch (error) 
    {
      console.error('Error:', error);
    }
    setInput(''); 
  };

  const handleButtonClick = (button) => 
  {
    // Kullanıcı butona tıkladığında başlığı mesaj olarak ekliyoruz
    const userMessage = { text: button.title, user: 'user' };
    setMessages((prevMessages) => [...prevMessages, userMessage]);
    setButtons([]); // Butonlar sıfırlanıyor
    sendMessage(button.payload, true); // Payload'u sadece arka planda sunucuya gönderiyoruz
  };

  useEffect(() => 
  {
    if (chatWindowRef.current) 
    {
      chatWindowRef.current.scrollTop = chatWindowRef.current.scrollHeight;
    }
  }, [messages]);

  return (
    <div className="App">
      <div className="chat-header">
        AndroAI
      </div>
      <div className="chat-window" ref={chatWindowRef}>
        {/* Mesajlar */}
        {messages.map((message, index) => (
          <div key={index} className={`message ${message.user}`}>
            {message.text} {/* Sadece text alanı basılıyor */}
          </div>
        ))}

        {/* Butonlar */}
        {buttons.length > 0 && (
          <div className="buttons-container">
            {buttons.map((button, index) => (
              <button key={index} className="button" onClick={() => handleButtonClick(button)}>
                {button.title} {/* Payload değil sadece title ekrana basılıyor */}
              </button>
            ))}
          </div>
        )}
      </div>
      <div className="input-container">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' && sendMessage(input)}
          placeholder="Type your message..."
        />
        <button 
          style={{ fontWeight: 'bold', fontSize: '19px' }} 
          onClick={() => sendMessage(input)}
        >
          Send
        </button>
      </div>
    </div>
  );
}

export default App;
