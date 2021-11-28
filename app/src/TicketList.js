import Ticket from './Ticket'
import React ,{useState, useEffect } from 'react';
import axios from 'axios';



const renderTicketData = (data) => {
    return (
        <ul>
            {
                data.map((item, index) => {
                    return <li key={index} >{item.subject}</li>
                })
            }
        </ul>
    )
}

const TicketList = () => {

    const [tickets, setTickets] = useState([]);
    const [currentPage, setCurrentPage] = useState(1);
    const [itemsPerPage, setItemsPerPage] = useState(25);

    const handleClick = (event) => {
        setCurrentPage(Number(event.target.id));
      };

    const pages = [];
    for(let i=1; i<=Math.ceil(tickets.length)/itemsPerPage;i++){
        pages.push(i);
    }

    const indexOfLastItem = currentPage*itemsPerPage;
    const indexOfFirstItem = indexOfLastItem - itemsPerPage;
    const currentItems = tickets.slice(indexOfFirstItem, indexOfLastItem);

    const renderPageNumbers = pages.map(number=>{
        return (
            <li key={number} id={number} onClick={handleClick}>
                {number}
            </li>
        )
    })

    useEffect(() => {
        fetchTickets();
      }, []);

    const fetchTickets = () => {
        axios
          .get('/tickets')
          .then((res) => {
              console.log(res.data);
            setTickets(res.data.tickets);
          })
          .catch((err) => {
            console.log(err);
          });
      };

    return (
        <>

        <h1>Tickets List</h1>
        <ul className='pageNumbers'>{renderPageNumbers}</ul>
        {renderTicketData(currentItems)}

        
        </>
    )
}

 export default TicketList