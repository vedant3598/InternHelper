# importing IndeedClient library from Indeed's API
from indeed import IndeedClient
# importing us library to get list of US states
import us
# import socket to be able to access IP address of user
import socket

# Initiating an IndeedClient object
client = IndeedClient(publisher = '')

# Client IP address to get IP address of user (required for 'userip' of parameter request to Indeed API)
client_hostname = socket.gethostname()
client_ip_address = socket.gethostbyname(client_hostname)

def position_location(location: str, position: str):
    parameters = {
        'q': "{position}",
        'l': "{location}",
        'fromage': "12",
        'limit': "25",
        'filter': "1",
        'userip': "{client_ip_address}",
        'useragent': ""
    }

    search_response = client.search(**parameters)
    return search_response

def position(position: str):
    us_states = getUSAStates

    for us_state in us_states:
        parameters = {
            'q': "{position}",
            'l': "{us_state}",
            'fromage': "12",
            'limit': "25",
            'filter': "1",
            'userip': "{client_ip_address}",
            'useragent': ""
        }

        search_response = client.search(**parameters)
        return search_response

def getUSAStates():
    return us.states.State