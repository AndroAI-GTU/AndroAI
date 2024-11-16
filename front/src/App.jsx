import React, { useState, useEffect, useRef } from 'react';
import './App.css';
import { v4 as uuidv4 } from 'uuid'; /* we will create a unique id for each user with this */

function App() 
{
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [buttons, setButtons] = useState([]);
  const [userId, setUserId] = useState(null);  /* state for Unique ID */
  const chatWindowRef = useRef(null);

  useEffect(() => 
  {
    /* Check Unique ID from localStorage */
    let storedId = localStorage.getItem('userId');
    console.log("Assigned User ID:", storedId);

    if (!storedId) 
    {
      storedId = uuidv4();  /* creat an UUID */
      localStorage.setItem('userId', storedId);
    }
    setUserId(storedId);  /* save to State */

    /* wait for the first message after updating userId */
  }, [userId]);

  const sendMessage = async (message, ButtonsMessage=false) => 
  {
    if(!userId)
    {
      console.warn("User ID has not been defined yet, the operation is on hold.");
      return;
    }

    if (!message || message.trim() === '') return;

    /* add the user message */
    const userMessage = { text: message, user: 'user' };

    /* Only title is printed on the screen */
    if (!ButtonsMessage) setMessages((prevMessages) => [...prevMessages, userMessage]);

    console.log("Sending message:", message);

    try 
    {
      console.log("Sending message:", message, "User ID:", userId);

      const response = await fetch('http://localhost:5001/chat', 
      {
        method: 'POST',
        headers: 
        {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': '*',
        },
        body: JSON.stringify({ message: message, userId: userId }), /* userId'yi de sunucuya gönderiyoruz */
      });

      const data = await response.json();
      console.log("JSON parsed:", data);

      /* Check if the message is array */
      const responseData = Array.isArray(data) ? data[0] : data;

      if (responseData.text) 
      {
        const botMessage = { text: responseData.text, user: 'bot' };
        setMessages((prevMessages) => [...prevMessages, botMessage]);
      }

      /* Check incoming buttons */
      if (responseData.buttons && responseData.buttons.length > 0) 
      {
        setButtons(responseData.buttons); /* Set if there are buttons */
      } 

      else 
      {
        setButtons([]); /* Reset if there are no buttons */
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
    /* Add the title as a message when the user clicks the button */
    const userMessage = { text: button.title, user: 'user' };
    setMessages((prevMessages) => [...prevMessages, userMessage]);
    setButtons([]); /* reset the buttons */
    sendMessage(button.payload, true);
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
        {/* Messages */}
        {messages.map((message, index) => (
          <div key={index} className={`message ${message.user}`}>
            {message.text} {/* Sadece text alanı basılıyor */}
          </div>
        ))}

        {/* Buttons */}
        {buttons.length > 0 && (
          <div className="buttons-container">
            {buttons.map((button, index) => (
              <button key={index} className="button" onClick={() => handleButtonClick(button)}>
                {button.title} {/* Not payload, only title is printed on the screen */}
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
