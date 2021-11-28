from flask_restful import Resource
from flask import request
from app.services.zendesk_api_service import ZendeskApiService
from app.database import zendesk_config
from flasgger import swag_from


class Tickets(Resource):

    @staticmethod
    @swag_from('swagger/tickets.yml')
    def get():
        zendesk_service = ZendeskApiService(zendesk_config)
        tickets = zendesk_service.get_tickets()
        return tickets

class Ticket(Resource):

    @staticmethod
    @swag_from('swagger/ticket.yml')
    def get(id):
        zendesk_service = ZendeskApiService(zendesk_config)
        ticket, status_code = zendesk_service.get_ticket(id)
        if status_code == 200:
            return ticket
        return ticket