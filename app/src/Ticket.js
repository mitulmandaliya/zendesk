import React from 'react';
import { Modal, Button, Form } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.css";

const Ticket = ({ticket, ticketdata}) => {

    const [show, setShow] = useState(false);
    const handleShow = () => setShow(true);
    const handleClose = () => setShow(false);

    return (
        <div>
            <h3 onClick={handleShow}>{ticketdata.subject}</h3>
            <Modal show={show}>
            <Modal.Header closeButton>
            <Modal.Title>Login Form</Modal.Title>
            </Modal.Header>
            <Modal.Body>
            <></>
            </Modal.Body>
            <Modal.Footer>
            <Button variant="secondary">Close Modal</Button>
            </Modal.Footer>
        </Modal>
        </div>

        
    )
}

export default Ticket