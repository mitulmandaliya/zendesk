import logo from './logo.svg';
import React from 'react';
import './App.css';
import { useState } from "react"
import TicketList from './TicketList'



const App = () => {

  const [tickets, setTickets] = useState([
    {
        id: 1,
        name: 'test ticket 1'
    },
    {
        id: 2,
        name: 'test ticket 2'
    }
  ])

  return (
    <div className="App">
      <div className="App-header">
      <TicketList tickets={tickets}/>
      </div>
      
    </div>
  );
}

export default App;
