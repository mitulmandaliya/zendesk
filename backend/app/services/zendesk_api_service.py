import requests
import base64
from requests.auth import HTTPBasicAuth
import os

class BasicAuth():
    '''
        BasicAuth for Zendesk service
    '''

    def __init__(self, user, api_token):
        self._user = user
        self._api_token = api_token

    def get_auth(self):
        base_string = base64.b64encode(
            bytes(f'{self._user}/token:{self._api_token}', 'utf-8')).decode("utf-8")
        return 'Basic '+base_string

    def headers(self):
        return {'content-type': "application/json",
                'Authorization': self.get_auth()}

def auth_factory(auth_config):
    return BasicAuth(auth_config.get('username'),
                     auth_config.get('api_token'))

class ZendeskApiService:

    def __init__(self, configuration: dict):
        self._base_url = configuration.get('base_url')

        if not self._base_url:
            raise Exception(f'Zendesk base URL is empty')

        auth_config = configuration.get("basic_auth")
        self._auth = auth_factory(auth_config)
        self._config = configuration

    def _get(self, url_suffix: str):
        return requests.get(self._base_url + url_suffix,
                            headers=self._auth.headers())

    def get_tickets(self):
        try:
            response = self._get(f'/tickets')
            if response.ok:
                return response.json(), response.status_code
            else:
                return response.text, response.status_code
        except Exception as e:
            raise e

    def get_ticket(self, id):
        try:
            response = self._get(f'/tickets/{id}')
            if response.ok:
                ticket = response.json().get('ticket')
                ticket_details = {}
                ticket_details['id'] = ticket.get('id')
                ticket_details['priority'] = ticket.get('priority')
                ticket_details['requester_id'] = ticket.get('requester_id')
                ticket_details['subject'] = ticket.get('subject')
                ticket_details['raw_subject'] = ticket.get('raw_subject')
                ticket_details['description'] = ticket.get('description')
                ticket_details['status'] = ticket.get('status')
                ticket_details['created_at'] = ticket.get('created_at')
                ticket_details['updated_at'] = ticket.get('updated_at')

                return ticket, response.status_code
            else:
                return response.text, response.status_code
        except Exception as e:
            raise e
